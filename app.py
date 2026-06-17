from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
import os
import replicate

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/create-video/")
async def create_ai_video(request: Request):
    try:
        data = await request.json()
        prompt = data.get("prompt", "a cinematic shot")
        
        # Replicate mijozini yaratish
        client = replicate.Client(api_token=os.getenv("REPLICATE_API_TOKEN"))
        
        # Modelni ishga tushirish
        output = client.run(
            "stability-ai/stable-video-diffusion:3f045789",
            input={"input_image": prompt}
        )
        return JSONResponse(content={"status": "success", "data": str(output)})
    
    except Exception as e:
        # Xatoni ekranga chiqarish uchun JSON formatda qaytaramiz
        return JSONResponse(content={"status": "error", "message": str(e)}, status_code=500)
