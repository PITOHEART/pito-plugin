from fastapi import FastAPI, Header, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import datetime, uuid

app = FastAPI(
    title="Pito Memory API",
    version="1.0.0",
    description="会話ログのインジェスト＆リトリーブエンドポイント",    
    servers=[{"url": "https://1282-124-101-197-80.ngrok-free.app"}],  # ← ここを追加    
)
    
# 静的ファイルを配信
app.mount("/", StaticFiles(directory=".well-known"), name="static")

class Record(BaseModel):
    id: str
    speaker: str
    timestamp: datetime.datetime
    text: str

@app.post("/ingest")
async def ingest(record: Record, authorization: str = Header(...)):
    if authorization != "Bearer secret1234":
        raise HTTPException(status_code=401, detail="Unauthorized")
    # TODO: data/raw に保存するロジックをここに書く
    return {"status": "ok"}

class RetrieveQuery(BaseModel):
    query: str

@app.post("/retrieve")
async def retrieve(q: RetrieveQuery, authorization: str = Header(...)):
    if authorization != "Bearer secret1234":
        raise HTTPException(status_code=401, detail="Unauthorized")
    # TODO: ベクトル検索結果をここで返す
    return [{"id": "sample_1", "text": "過去ログ例", "score": 0.99}]
