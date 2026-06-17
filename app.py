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
async def create_ai_video(request: Request):
    try:
        # Tokenni Render muhitidan olamiz
        token = os.environ.get("REPLICATE_API_TOKEN")
        if not token:
            return JSONResponse(status_code=500, content={"error": "API Token Render'da sozlanmagan!"})
        
        data = await request.json()
        prompt = data.get("prompt", "a cinematic landscape")
        
        # Modelni chaqirish
        client = replicate.Client(api_token=token)
        output = client.run(
            "stability-ai/sdxl:39ed52f2",
            input={"prompt": prompt}
        )
        return {"result": str(output[0])}
    
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
