import os
import replicate
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.post("/create-video/")
async def create_video(request: Request):
    try:
        # Tokenni Render'dan o'qiymiz
        token = os.getenv("REPLICATE_API_TOKEN")
        if not token:
            return JSONResponse(status_code=500, content={"error": "API Token topilmadi"})
            
        data = await request.json()
        prompt = data.get("prompt", "a cat")
        
        # Modelni ishlatish
        client = replicate.Client(api_token=token)
        output = client.run(
            "stability-ai/stable-video-diffusion:3f045789",
            input={"input_image": prompt}
        )
        return {"video_url": str(output)}
        
    except Exception as e:
        # Xatoni aniq ko'ramiz
        return JSONResponse(status_code=500, content={"error": str(e)})
