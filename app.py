from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <!DOCTYPE html>
    <html lang="uz">
    <head>
        <style>
            body { background-color: #0f172a; color: white; font-family: 'Segoe UI', sans-serif; display: flex; flex-direction: column; align-items: center; padding: 20px; }
            .container { background: #1e293b; padding: 30px; border-radius: 20px; width: 100%; max-width: 500px; text-align: center; }
            input { width: 80%; padding: 12px; border-radius: 8px; border: none; margin-bottom: 10px; }
            button { background: #38bdf8; color: #0f172a; border: none; padding: 12px 25px; border-radius: 8px; font-weight: bold; cursor: pointer; margin: 5px; }
            #result { margin-top: 20px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>AI Media Fabrika</h1>
            <input type="text" id="prompt" placeholder="Mavzuni yozing...">
            <br>
            <button onclick="genArt()">Rasm Yaratish</button>
            <button onclick="genVideo()" style="background:#fbbf24;">Video Yaratish (Beta)</button>
            <div id="result"></div>
        </div>
        <script>
            function genArt() {
                const prompt = document.getElementById("prompt").value;
                document.getElementById("result").innerHTML = `<img src="https://image.pollinations.ai/prompt/${encodeURIComponent(prompt)}?seed=42" style="max-width:100%; border-radius:15px;">`;
            }
            function genVideo() {
                const prompt = document.getElementById("prompt").value;
                document.getElementById("result").innerHTML = "Video tayyorlanmoqda... (Hugging Face API orqali)";
                // Bu yerda video generation linki
                const vidUrl = `https://pollinations.ai/p/${encodeURIComponent(prompt)}?model=video&seed=42`;
                document.getElementById("result").innerHTML = `<video src="${vidUrl}" controls autoplay loop style="max-width:100%; border-radius:15px;"></video>`;
            }
        </script>
    </body>
    </html>
    """
