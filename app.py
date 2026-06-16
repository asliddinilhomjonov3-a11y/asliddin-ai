from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# HTML fayllar turgan papkani ulash
templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/create-video/")
async def create_ai_video(prompt: str, user_id: str):
    # Bu yerda video yasash mantig'i bo'ladi
    return {"message": f"Video tayyorlanmoqda: {prompt}", "status": "processing"}
