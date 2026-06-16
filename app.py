import os
import replicate
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
# templates papkasi loyihangizning ildizida ekanligiga ishonch hosil qiling
templates = Jinja2Templates(directory="templates")

# API tokeni Render muhitidan yuklanadi
os.environ["REPLICATE_API_TOKEN"] = os.getenv("REPLICATE_API_TOKEN", "")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    # Yangi FastAPI versiyalari uchun to'g'ri format
    return templates.TemplateResponse(
        request=request, name="index.html", context={}
    )

@app.post("/create-video/")
async def create_ai_video(request: Request):
    try:
        data = await request.json()
        prompt = data.get("prompt", "a beautiful landscape")
        
        output = replicate.run(
            "stability-ai/stable-video-diffusion:3f045789",
            input={"input_image": prompt}
        )
        return {"video_url": output}
    except Exception as e:
        return {"error": str(e)}
