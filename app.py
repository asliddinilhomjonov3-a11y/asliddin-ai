from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <html>
    <body>
        <h2>AI Bepul Rasm/Video Fabrika</h2>
        <input type="text" id="prompt" placeholder="Mavzu (inglizcha)...">
        <button onclick="createArt()">Yaratish</button>
        <p id="result"></p>
        <script>
            async function createArt() {
                const resEl = document.getElementById("result");
                const prompt = document.getElementById("prompt").value;
                resEl.innerText = "Yaratilmoqda...";
                
                // Pollinations.ai bepul API manzili
                const imageUrl = `https://pollinations.ai/p/${encodeURIComponent(prompt)}?width=768&height=768&seed=42`;
                
                resEl.innerHTML = `<br><img src="${imageUrl}" style="max-width:400px;"><br><a href="${imageUrl}" target="_blank">Rasmni yuklab olish</a>`;
            }
        </script>
    </body>
    </html>
    """
