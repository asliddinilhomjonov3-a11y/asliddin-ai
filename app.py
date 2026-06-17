from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import os
import replicate

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Tokeningizni oling
os.environ["REPLICATE_API_TOKEN"] = os.getenv("REPLICATE_API_TOKEN", "")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.post("/create-video/")
async def create_ai_video(request: Request):
    try:
        data = await request.json()
        prompt = data.get("prompt", "a cat")
        
        # Modelni ishga tushirish
        output = replicate.run(
            "stability-ai/stable-video-diffusion:3f045789",
            input={"input_image": prompt}
        )
        
        # Natijani oddiy matn sifatida qaytaramiz (video_url kalitisiz)
        return {"result": str(output)} 
    except Exception as e:
        return {"result": "Xatolik: " + str(e)}
