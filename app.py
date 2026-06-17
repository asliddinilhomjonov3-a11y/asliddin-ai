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
        <input type="text" id="prompt" placeholder="Masalan: futuristic city">
        <button onclick="createArt()">Yaratish</button>
        <div id="result" style="margin-top:20px;"></div>
        
        <script>
            function createArt() {
                const resEl = document.getElementById("result");
                const prompt = document.getElementById("prompt").value;
                resEl.innerHTML = "Rasm yaratilmoqda, kuting...";
                
                const imageUrl = `https://pollinations.ai/p/${encodeURIComponent(prompt)}?width=768&height=768&seed=42&nologo=true`;
                
                // Rasm yuklangandan keyin ko'rsatish
                const img = new Image();
                img.src = imageUrl;
                img.onload = () => {
                    resEl.innerHTML = `<img src="${imageUrl}" style="max-width:500px; border-radius:10px;"><br>
                                       <a href="${imageUrl}" target="_blank">Rasmni kattaroq ko'rish</a>`;
                };
            }
        </script>
    </body>
    </html>
    """
