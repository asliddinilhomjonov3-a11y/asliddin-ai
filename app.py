from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <!DOCTYPE html>
    <html lang="uz">
    <head>
        <meta charset="UTF-8">
        <style>
            body { background-color: #0f172a; color: white; font-family: 'Segoe UI', sans-serif; display: flex; flex-direction: column; align-items: center; padding: 20px; }
            h1 { color: #38bdf8; }
            .container { background: #1e293b; padding: 30px; border-radius: 20px; box-shadow: 0 10px 25px rgba(0,0,0,0.3); width: 100%; max-width: 500px; text-align: center; }
            input { width: 80%; padding: 12px; border-radius: 8px; border: none; margin-bottom: 10px; }
            button { background: #38bdf8; color: #0f172a; border: none; padding: 12px 25px; border-radius: 8px; font-weight: bold; cursor: pointer; transition: 0.3s; }
            button:hover { background: #7dd3fc; }
            #result { margin-top: 20px; }
            img { max-width: 100%; border-radius: 15px; border: 3px solid #38bdf8; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>AI Art Generator</h1>
            <input type="text" id="prompt" placeholder="Mavzuni yozing...">
            <br>
            <button onclick="generate()">Yaratish</button>
            <div id="result"></div>
        </div>
        <script>
            function generate() {
                const res = document.getElementById("result");
                const prompt = document.getElementById("prompt").value;
                res.innerHTML = "Jarayon ketmoqda, kuting...";
                const url = `https://image.pollinations.ai/prompt/${encodeURIComponent(prompt)}?width=768&height=768&seed=42&nologo=true`;
                res.innerHTML = `<br><img src="${url}" alt="AI Result">`;
            }
        </script>
    </body>
    </html>
    """
