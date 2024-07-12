### 雲育鏈面試作業

#### 作業說明

```
git clone git@github.com:dddong3/cxcxc_interview.git
cd cxcxc_interview
```
#### 環境設定
```
pip/pip3 install poetry
poetry install
poetry init
```

#### HW1
```
uvicorn HW1.src.main:app --host 0.0.0.0 --port 8000
or
docker build -t cxcxc_hw1 -f HW4/HW1.Dockerfile .
docker run --rm -p 8000:8000 -d cxcxc_hw1
```
visit http://127.0.0.1:8000/docs


#### HW2
```
uvicorn HW2.src.main:app --host 0.0.0.0 --port 8000
or
docker build -t cxcxc_hw2 -f HW4/HW2.Dockerfile .
docker run --rm -p 8000:8000 -d cxcxc_hw2
```
visit http://127.0.0.1:8000/docs

#### HW3
Copy .env.example to .env and fill the value
required value: 
- GEMINI_API_KEY
- LINE_CHANNEL_ACCESS_TOKEN
- LINE_CHANNEL_SECRET

```
uvicorn HW3.src.main:app --host 0.0.0.0 --port 8000
or
docker build -t cxcxc_hw3 -f HW4/HW3.Dockerfile .
docker run --rm -p 8000:8000 -d cxcxc_hw3
```
visit http://127.0.0.1:8000/docs