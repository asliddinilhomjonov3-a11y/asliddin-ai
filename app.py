from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

# 'templates' papkasi loyihangizning asosiy qismida ekanligiga ishonch hosil qiling
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home(request: Request):
    # Bu usul eng barqaror hisoblanadi
    return templates.TemplateResponse(
        request=request, 
        name="index.html"
    )

@app.post("/create-video/")
async def create_ai_video(prompt: str, user_id: str):
    return {"message": f"Video tayyorlanmoqda: {prompt}", "status": "processing"}
