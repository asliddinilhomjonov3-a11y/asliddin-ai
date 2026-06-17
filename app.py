from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# 10 000+ shablonni boshqarish uchun struktura (Buni xohlagancha kengaytiring!)
TEMPLATES = [
    {"category": "Cinematic", "name": "Hollywood Style", "prompt": "cinematic, 8k, movie lighting"},
    {"category": "Cinematic", "name": "Noir", "prompt": "black and white, moody, film noir"},
    {"category": "Anime", "name": "Studio Ghibli", "prompt": "anime style, Ghibli, vibrant, detailed"},
    {"category": "Anime", "name": "Cyberpunk Anime", "prompt": "anime, cyberpunk, neon, future, detailed"},
    {"category": "3D", "name": "Claymation", "prompt": "claymation style, cute, stop motion"},
    {"category": "3D", "name": "Unreal Engine 5", "prompt": "3d render, unreal engine 5, photorealistic"},
    {"category": "Art", "name": "Van Gogh", "prompt": "oil painting, Van Gogh style, thick paint"},
    {"category": "Art", "name": "Sketch", "prompt": "pencil sketch, artistic, minimal"},
    # Bu yerga yana minglab qo'shishingiz mumkin...
]

@app.get("/", response_class=HTMLResponse)
async def home():
    # Kategoriyalar bo'yicha saralash
    categories = sorted(list(set(t["category"] for t in TEMPLATES)))
    options = "".join([f'<option value="{t["prompt"]}">{t["category"]} | {t["name"]}</option>' for t in TEMPLATES])
    
    return f"""
    <!DOCTYPE html>
    <html lang="uz">
    <head>
        <style>
            body {{ background: #050505; color: #fff; font-family: 'Segoe UI', sans-serif; display: flex; justify-content: center; padding: 20px; }}
            .panel {{ background: #111; padding: 30px; border-radius: 20px; width: 100%; max-width: 600px; border: 1px solid #333; }}
            h1 {{ text-align: center; color: #38bdf8; }}
            input, select {{ width: 100%; padding: 15px; margin: 10px 0; background: #1a1a1a; color: white; border: 1px solid #333; border-radius: 10px; }}
            .action-btn {{ width: 100%; padding: 15px; background: #38bdf8; border: none; color: black; font-weight: bold; border-radius: 10px; cursor: pointer; }}
        </style>
    </head>
    <body>
        <div class="panel">
            <h1>AiVid Studio Pro</h1>
            <input type="text" id="prompt" placeholder="Mavzuni yozing...">
            <select id="template">{options}</select>
            <button class="action-btn" onclick="run()">Yaratish</button>
            <div id="result" style="margin-top:20px;"></div>
        </div>
        <script>
            function run() {{
                const p = document.getElementById("prompt").value;
                const t = document.getElementById("template").value;
                const url = `https://pollinations.ai/p/${{encodeURIComponent(p + ', ' + t)}}?model=video&seed=42`;
                document.getElementById("result").innerHTML = `<video src="${{url}}" controls autoplay loop style="width:100%; border-radius:15px;"></video>`;
            }}
        </script>
    </body>
    </html>
    """
