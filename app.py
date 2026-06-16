from fastapi import FastAPI, HTTPException

app = FastAPI()

user_credits = {"dasturchi_1": 100}

@app.get("/")
def home():
    return {"status": "AI Video Fabrika ishga tushdi", "docs": "http://127.0.0.1:8000/docs manzili orqali API ni ko'rishing mumkin"}

@app.post("/create-video/")
async def create_ai_video(prompt: str, user_id: str):
    if user_id not in user_credits or user_credits[user_id] <= 0:
        raise HTTPException(status_code=403, detail="Kredit tugadi, obuna bo'ling!")
    
    return {"message": f"Video tayyorlanmoqda: {prompt}", "status": "processing"}