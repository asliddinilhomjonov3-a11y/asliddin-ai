from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import replicate
import os

app = FastAPI()
# templates papkasi loyihangizning asosiy qismida bo'lishi kerak
templates = Jinja2Templates(directory="templates")

# API tokeni Render'dan olinadi
os.environ["REPLICATE_API_TOKEN"] = os.getenv("REPLICATE_API_TOKEN", "")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/create-video/")
async def create_ai_video(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "a beautiful landscape")
    
    # AI modelini chaqirish
    output = replicate.run(
        "stability-ai/stable-video-diffusion:3f045789",
        input={"input_image": prompt} 
    )
    return {"video_url": output}
