from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import replicate
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# API tokeningiz Render'da o'rnatilganiga ishonch hosil qiling
os.environ["REPLICATE_API_TOKEN"] = os.getenv("REPLICATE_API_TOKEN", "")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/create-video/")
async def create_ai_video(request: Request):
    try:
        # Frontdan kelgan ma'lumotni o'qish
        data = await request.json()
        prompt_text = data.get("prompt", "a beautiful landscape")
        
        # AI chaqiruvi
        output = replicate.run(
            "stability-ai/stable-video-diffusion:3f045789",
            input={"input_image": prompt_text}
        )
        
        # Natijani logga chiqaramiz (Render Logs bo'limida ko'rishingiz mumkin)
        print("AI chiqishi:", output)
        
        # Agar natija ro'yxat bo'lsa, birinchi elementni olamiz
        video_url = str(output[0]) if isinstance(output, list) else str(output)
        
        return {"video_url": video_url}
    except Exception as e:
        # Xatoni aniq yozib qaytaramiz
        return {"error": str(e)}
