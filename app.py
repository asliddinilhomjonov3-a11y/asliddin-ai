from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import replicate
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

os.environ["REPLICATE_API_TOKEN"] = os.getenv("REPLICATE_API_TOKEN", "")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/create-video/")
async def create_ai_video(request: Request):
    try:
        data = await request.json()
        prompt_text = data.get("prompt", "a beautiful landscape")
        
        output = replicate.run(
            "stability-ai/stable-video-diffusion:3f045789",
            input={"input_image": prompt_text} 
        )
        return {"video_url": output}
    except Exception as e:
        return {"error": str(e)}
