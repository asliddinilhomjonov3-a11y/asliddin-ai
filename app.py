from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse
import os
import replicate

app = FastAPI()
templates = Jinja2Templates(directory="templates")

os.environ["REPLICATE_API_TOKEN"] = os.getenv("REPLICATE_API_TOKEN", "")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.post("/create-video/")
async def create_ai_video(request: Request):
    try:
        data = await request.json()
        prompt = data.get("prompt", "a cinematic shot of a sunset")
        
        # Replicate modelini chaqirish
        client = replicate.Client(api_token=os.getenv("REPLICATE_API_TOKEN"))
        output = client.run(
            "stability-ai/stable-video-diffusion:3f045789",
            input={"input_image": prompt}
        )
        return JSONResponse(content={"status": "success", "data": str(output)})
    except Exception as e:
        # Xatolikni JSON formatda qaytarish
        return JSONResponse(content={"status": "error", "message": str(e)}, status_code=500)
