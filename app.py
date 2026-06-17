import os
import replicate
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home(request: Request):
    # YANGI USUL: request argumentini alohida berish kerak
    return templates.TemplateResponse(request=request, name="index.html")

@app.post("/create-video/")
async def create_video(request: Request):
    try:
        # Token mavjudligini tekshirish
        token = os.getenv("REPLICATE_API_TOKEN")
        if not token:
            return JSONResponse(status_code=500, content={"error": "API Token topilmadi!"})
            
        data = await request.json()
        prompt = data.get("prompt", "a cinematic shot")
        
        # Replicate modelini chaqirish (SDXL matndan rasm yasash modeli)
        client = replicate.Client(api_token=token)
        output = client.run(
            "stability-ai/sdxl:39ed52f2",
            input={"prompt": prompt}
        )
        
        return {"result": str(output[0] if isinstance(output, list) else output)}
        
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
