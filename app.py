import os
import replicate
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, HTMLResponse

app = FastAPI()

# HTMLni alohida fayldan emas, to'g'ridan-to'g'ri koddan qaytaramiz (xatolarni kamaytirish uchun)
@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <html>
    <body>
        <input type="text" id="prompt" placeholder="Mavzu...">
        <button onclick="createVideo()">Video yasash</button>
        <p id="result"></p>
        <script>
            async function createVideo() {
                const resEl = document.getElementById("result");
                resEl.innerText = "Kuting...";
                try {
                    const response = await fetch("/api/video/", {
                        method: "POST",
                        headers: {"Content-Type": "application/json"},
                        body: JSON.stringify({prompt: document.getElementById("prompt").value})
                    });
                    const data = await response.json();
                    resEl.innerText = data.msg;
                } catch(e) { resEl.innerText = "Xato!"; }
            }
        </script>
    </body>
    </html>
    """

@app.post("/api/video/")
async def create_video(request: Request):
    try:
        token = os.getenv("REPLICATE_API_TOKEN")
        if not token: return {"msg": "XATO: API Token topilmadi!"}
        
        data = await request.json()
        prompt = data.get("prompt")
        
        client = replicate.Client(api_token=token)
        output = client.run("stability-ai/sdxl:39ed52f2", input={"prompt": prompt})
        return {"msg": "Natija: " + str(output)}
    except Exception as e:
        return {"msg": "SERVER XATOSI: " + str(e)}
