from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <!DOCTYPE html>
    <html>
    <body>
        <h2>AI Bepul Rasm Fabrikasi</h2>
        <input type="text" id="prompt" value="futuristic city">
        <button onclick="createArt()">Yaratish</button>
        <div id="result" style="margin-top:20px;"></div>
        
        <script>
            function createArt() {
                const resEl = document.getElementById("result");
                const prompt = document.getElementById("prompt").value;
                // 'https' ishlatamiz
                const url = `https://image.pollinations.ai/prompt/${encodeURIComponent(prompt)}?width=512&height=512&seed=42`;
                
                resEl.innerHTML = `<img src="${url}" style="border: 2px solid green; max-width: 500px;">`;
            }
        </script>
    </body>
    </html>
    """
