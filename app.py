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
async def create_ai_video(request: Request):
    try:
        # Tokenni muhitdan olish
        token = os.getenv("REPLICATE_API_TOKEN")
        if not token:
            return JSONResponse(content={"error": "API Token topilmadi!"}, status_code=500)
            
        data = await request.json()
        prompt = data.get("prompt", "a cat")
        
        # Modelni chaqirish
        client = replicate.Client(api_token=token)
        output = client.run(
            "stability-ai/sdxl:39ed52f2",
            input={"prompt": prompt}
        )
        
        return {"video_url": output[0] if isinstance(output, list) else output}
    
    except Exception as e:
        # Xatoni ekranga aniq chiqarish
        return JSONResponse(content={"error": str(e)}, status_code=500)
