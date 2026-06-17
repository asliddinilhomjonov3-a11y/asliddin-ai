import os
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
import replicate

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/create-video/")
async def create_video(request: Request):
    try:
        api_token = os.getenv("REPLICATE_API_TOKEN")
        if not api_token:
            return JSONResponse(status_code=500, content={"error": "API Token topilmadi"})
            
        data = await request.json()
        prompt = data.get("prompt", "a cat")
        
        # SDXL modeli matn qabul qiladi
        client = replicate.Client(api_token=api_token)
        output = client.run(
            "stability-ai/sdxl:39ed52f2",
            input={"prompt": prompt}
        )
        return {"video_url": output[0] if isinstance(output, list) else output}
        
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
