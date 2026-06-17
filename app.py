import os
import replicate
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse

app = FastAPI()
# templates papkasi to'g'ri ko'rsatilganligiga ishonch hosil qiling
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home(request: Request):
    # ESKI (XATO) USUL: return templates.TemplateResponse("index.html", {"request": request})
    # YANGI (TO'G'RI) USUL:
    return templates.TemplateResponse(request=request, name="index.html")

@app.post("/create-video/")
async def create_video(request: Request):
    try:
        token = os.getenv("REPLICATE_API_TOKEN")
        data = await request.json()
        prompt = data.get("prompt", "a cinematic shot")
        
        client = replicate.Client(api_token=token)
        output = client.run(
            "stability-ai/stable-video-diffusion:3f045789",
            input={"input_image": prompt}
        )
        return {"status": "success", "data": str(output)}
    except Exception as e:
        return {"status": "error", "message": str(e)}
