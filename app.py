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
        data = await request.json()
        prompt = data.get("prompt", "a cinematic shot of a sunset")
        
        # SDXL modeli matn qabul qiladi, bu kod aniq ishlaydi
        client = replicate.Client(api_token=os.getenv("REPLICATE_API_TOKEN"))
        output = client.run(
            "stability-ai/sdxl:39ed52f2",
            input={"prompt": prompt}
        )
        # SDXL rasm qaytaradi, uni ro'yxatdan olamiz
        image_url = output[0] if isinstance(output, list) else output
        return {"video_url": str(image_url)}
        
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
