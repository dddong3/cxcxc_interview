import os

import google.generativeai as genai
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request
from linebot.v3 import WebhookHandler
from linebot.v3.exceptions import InvalidSignatureError
from linebot.v3.messaging import (
    ApiClient,
    Configuration,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage,
)
from linebot.v3.webhooks import MessageEvent, TextMessageContent
from pydantic import BaseModel

load_dotenv(".env", override=True, encoding="utf-8")

configuration = Configuration(access_token=os.getenv("LINE_CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(os.getenv("LINE_CHANNEL_SECRET"))

app = FastAPI()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
GENAI_MODEL = genai.GenerativeModel("gemini-1.5-flash")


def generate_text(prompt: str):
    ai_prompt = """
只幫我解析文句中的 姓名 / 體重 / 身高三樣屬性，並且將這三樣屬性的值已下列格式回傳，若沒有該屬性則該屬性回傳None：
[姓名]/[體重]/[身高]
"""
    prompt = ai_prompt + prompt
    result = GENAI_MODEL.generate_content(prompt)
    print(result.text)
    return result.text


def parse_text(text: str):
    result_text = text.split("/")
    return {
        "name": result_text[0].strip(),
        "weight": result_text[1].strip(),
        "height": result_text[2].strip(),
    }


class LLMRequest(BaseModel):
    text: str


@app.post("/llm")
async def llm(payload: LLMRequest):
    result = generate_text(payload.text)
    return parse_text(result)


@app.post("/callback")
async def callback(request: Request):
    signature = request.headers.get("X-Line-Signature")
    body = await request.body()
    try:
        handler.handle(body.decode(), signature)
    except InvalidSignatureError:
        raise HTTPException(status_code=400, detail="Invalid signature")
    return "OK"


@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        user_message = event.message.text
        response_text = generate_text(user_message)
        reply_message = parse_text(response_text)
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[TextMessage(text=f"姓名: {reply_message['name']}, 體重: {reply_message['weight']}, 身高: {reply_message['height']}")],
            )
        )
