from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            img { max-width: 500px; margin-top: 20px; border: 2px solid #ccc; }
        </style>
    </head>
    <body>
        <h2>AI Bepul Rasm Fabrikasi</h2>
        <input type="text" id="prompt" placeholder="Masalan: A beautiful landscape">
        <button onclick="createArt()">Yaratish</button>
        <div id="result"></div>
        
        <script>
            function createArt() {
                const resEl = document.getElementById("result");
                const prompt = document.getElementById("prompt").value;
                const encodedPrompt = encodeURIComponent(prompt);
                
                resEl.innerHTML = "Rasm yuklanmoqda...";
                
                // Rasmni sahifaga qo'shamiz
                const imgUrl = `https://pollinations.ai/p/${encodedPrompt}?width=768&height=768&seed=42`;
                resEl.innerHTML = `<br><img src="${imgUrl}" alt="AI Rasm">`;
            }
        </script>
    </body>
    </html>
    """
