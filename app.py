from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import os
import replicate

app = FastAPI()
# templates papkasi loyiha ildizida ekanligiga ishonch hosil qiling
templates = Jinja2Templates(directory="templates")

# API Token
os.environ["REPLICATE_API_TOKEN"] = os.getenv("REPLICATE_API_TOKEN", "")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    # Bu format ko'pchilik versiyalarda ishlaydi
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/create-video/")
async def create_ai_video(request: Request):
    try:
        data = await request.json()
        prompt = data.get("prompt", "a cinematic shot of a sunset")
        
        # Replicate AI chaqiruvi
        output = replicate.run(
            "stability-ai/stable-video-diffusion:3f045789",
            input={"input_image": prompt}
        )
        return {"video_url": str(output)}
    except Exception as e:
        return {"error": str(e)}
