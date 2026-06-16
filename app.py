import os
import replicate
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

# templates papkasini topish
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

# API tokenni yuklash
os.environ["REPLICATE_API_TOKEN"] = os.getenv("REPLICATE_API_TOKEN", "")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/create-video/")
async def create_ai_video(request: Request):
    try:
        data = await request.json()
        prompt = data.get("prompt", "a beautiful landscape")
        
        # AI chaqiruvi
        output = replicate.run(
            "stability-ai/stable-video-diffusion:3f045789",
            input={"input_image": prompt}
        )
        return {"video_url": output}
    except Exception as e:
        return {"error": str(e)}
