import os
import replicate
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.post("/create-video/")
async def create_ai_video(request: Request):
    # Frontend'dan kelgan ma'lumotni olish
    data = await request.json()
    prompt = data.get("prompt")
    
    # Replicate API orqali modelni chaqirish
    # Muhim: Model nomi va versiyasi Replicate'dan olinadi
    output = replicate.run(
        "stability-ai/stable-video-diffusion:3f045789", 
        input={"input_image": prompt} 
    )
    return {"video_url": output}
