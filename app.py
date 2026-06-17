import os
import replicate
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/create-video/")
async def create_video(request: Request):
    try:
        # Tokenni to'g'ridan-to'g'ri os.getenv dan olamiz
        token = os.getenv("REPLICATE_API_TOKEN")
        data = await request.json()
        prompt = data.get("prompt", "a cinematic shot")
        
        # Modelni ishga tushirish
        client = replicate.Client(api_token=token)
        output = client.run(
            "stability-ai/stable-video-diffusion:3f045789",
            input={"input_image": prompt}
        )
        return {"status": "success", "data": str(output)}
    except Exception as e:
        return {"status": "error", "message": str(e)}
