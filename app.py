import os
import replicate
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI()

# HTML faylni to'g'ridan-to'g'ri o'qib beramiz
@app.get("/", response_class=HTMLResponse)
async def home():
    with open("templates/index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/create-video/")
async def create_video(request: Request):
    try:
        token = os.getenv("REPLICATE_API_TOKEN")
        if not token:
            return JSONResponse(status_code=500, content={"error": "Token yo'q!"})
            
        data = await request.json()
        prompt = data.get("prompt", "a cat")
        
        client = replicate.Client(api_token=token)
        output = client.run(
            "stability-ai/sdxl:39ed52f2",
            input={"prompt": prompt}
        )
        url = output[0] if isinstance(output, list) else output
        return {"result": str(url)}
        
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
