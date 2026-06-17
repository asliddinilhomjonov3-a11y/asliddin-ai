from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import replicate
import os

app = FastAPI()
# "templates" papkasi loyihangizning asosiy papkasida ekanligiga ishonch hosil qiling
templates = Jinja2Templates(directory="templates")

# API tokenini Render muhitidan oling
os.environ["REPLICATE_API_TOKEN"] = os.getenv("REPLICATE_API_TOKEN", "")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    # E'tibor bering: request=request yozilishi shart
    return templates.TemplateResponse(request=request, name="index.html", context={})

@app.post("/create-video/")
async def create_ai_video(request: Request):
    try:
        data = await request.json()
        prompt_text = data.get("prompt", "a cinematic shot of a sunset")
        
        output = replicate.run(
            "stability-ai/stable-video-diffusion:3f045789",
            input={"input_image": prompt_text}
        )
        return {"video_url": str(output)}
    except Exception as e:
        return {"error": str(e)}
