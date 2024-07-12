from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from HW2.src.controllers.user import router as user_router

app = FastAPI(prefix="/api")
app.include_router(user_router)


register_tortoise(
    app,
    generate_schemas=True,
    config={
        "connections": {
            "default": "sqlite://LEADERTUTOR.sqlite3",
        },
        "apps": {
            "models": {
                "models": ["HW2.src.models"],
                "default_connection": "default",
            }
        },
        "use_tz": False,
        "timezone": "Asia/Taipei",
    },
)
