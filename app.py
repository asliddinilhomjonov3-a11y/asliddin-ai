from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import replicate
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Tokenni Render muhitidan yuklash
os.environ["REPLICATE_API_TOKEN"] = os.getenv("REPLICATE_API_TOKEN", "")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html", context={})

@app.post("/create-video/")
async def create_ai_video(request: Request):
    try:
        data = await request.json()
        prompt = data.get("prompt", "a cinematic shot of a sunset")
        
        # AI chaqiruvi
        output = replicate.run(
            "stability-ai/stable-video-diffusion:3f045789",
            input={"input_image": prompt}
        )
        # Javobni to'g'ri formatda qaytarish
        return {"video_url": output}
    except Exception as e:
        return {"error": str(e)}
