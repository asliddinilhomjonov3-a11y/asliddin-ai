import os
import replicate
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse

app = FastAPI()
# templates papkasi borligini tekshiring
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/create-video/")
async def create_video(request: Request):
    try:
        # Tokenni muhitdan o'qish
        token = os.getenv("REPLICATE_API_TOKEN")
        if not token:
            return JSONResponse(status_code=500, content={"error": "API Token topilmadi"})
            
        data = await request.json()
        prompt = data.get("prompt", "a cinematic shot")
        
        # Replicate modelini chaqirish
        client = replicate.Client(api_token=token)
        output = client.run(
            "stability-ai/sdxl:39ed52f2",
            input={"prompt": prompt}
        )
        
        # Natijani qaytaramiz
        url = output[0] if isinstance(output, list) else output
        return {"result": str(url)}
        
    except Exception as e:
        # Xatoni aniq ko'rsatish
        return JSONResponse(status_code=500, content={"error": str(e)})
