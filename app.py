from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import replicate
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Tokenni Render muhitidan oling
os.environ["REPLICATE_API_TOKEN"] = os.getenv("REPLICATE_API_TOKEN", "")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html", context={})

@app.post("/create-video/")
async def create_ai_video(request: Request):
    try:
        data = await request.json()
        prompt_text = data.get("prompt", "a cinematic shot of a sunset")
        
        # AI chaqiruvi
        output = replicate.run(
            "stability-ai/stable-video-diffusion:3f045789",
            input={"input_image": prompt_text}
        )
        
        # Natijani logga chiqaring (Render Logs'da ko'rasiz)
        print("AI chiqishi:", output)
        
        return {"video_url": str(output)}
    except Exception as e:
        # Xatoni aniq qaytaramiz
        return {"error": str(e)}
