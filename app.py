from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# Bu yerga o'zingiz xohlagancha shablon qo'sha berasiz (istalgancha!)
TEMPLATES = [
    {"name": "Cinematic", "prompt": "cinematic, high quality, 8k, movie style"},
    {"name": "Anime", "prompt": "anime style, vibrant colors, studio ghibli, detailed"},
    {"name": "Cyberpunk", "prompt": "cyberpunk 2077 style, neon lights, futuristic city"},
    {"name": "Horror", "prompt": "spooky, dark, gothic, cinematic horror, eerie"},
    {"name": "Nature", "prompt": "lush nature, 4k, wildlife photography, realistic"},
    {"name": "3D Render", "prompt": "3d render, octane render, unreal engine 5, masterpiece"},
    {"name": "Sketch", "prompt": "pencil sketch, artistic drawing, detailed lines"},
    {"name": "Space", "prompt": "cosmic, galaxy, stars, nebula, space exploration"},
    {"name": "Retro", "prompt": "1990s vhs tape style, vintage, nostalgic"},
    {"name": "Luxury", "prompt": "elegant, luxury, gold, high fashion, professional"},
]

@app.get("/", response_class=HTMLResponse)
async def home():
    # Shablon tugmalarini avtomatik yaratish
    buttons_html = "".join([f'<button class="card" onclick="gen(\'{t["prompt"]}\')">{t["name"]}</button>' for t in TEMPLATES])
    
    return f"""
    <!DOCTYPE html>
    <html lang="uz">
    <head>
        <meta charset="UTF-8">
        <style>
            body {{ background-color: #0f172a; color: white; font-family: 'Segoe UI', sans-serif; display: flex; justify-content: center; padding: 20px; }}
            .container {{ background: #1e293b; padding: 30px; border-radius: 20px; width: 100%; max-width: 800px; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }}
            h1 {{ color: #38bdf8; }}
            input {{ width: 90%; padding: 15px; border-radius: 10px; border: none; margin-bottom: 20px; font-size: 16px; }}
            .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(130px, 1fr)); gap: 10px; margin-bottom: 20px; }}
            .card {{ background: #334155; border: none; padding: 12px; border-radius: 8px; color: white; cursor: pointer; transition: 0.3s; font-weight: bold; }}
            .card:hover {{ background: #38bdf8; transform: translateY(-3px); }}
            #result {{ margin-top: 20px; border-top: 2px solid #334155; padding-top: 20px; }}
            .loader {{ border: 4px solid #f3f3f3; border-top: 4px solid #38bdf8; border-radius: 50%; width: 30px; height: 30px; animation: spin 1s linear infinite; margin: 20px auto; }}
            @keyframes spin {{ 0% {{ transform: rotate(0deg); }} 100% {{ transform: rotate(360deg); }} }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>AiVid Studio</h1>
            <input type="text" id="prompt" placeholder="Videoni nima haqida bo'lishini yozing...">
            <div class="grid">{buttons_html}</div>
            <div id="result">Kutmoqdaman...</div>
        </div>
        <script>
            function gen(style) {{
                const p = document.getElementById("prompt").value;
                const finalPrompt = `${{p}}, ${{style}}`;
                document.getElementById("result").innerHTML = '<div class="loader"></div>';
                const v = `https://pollinations.ai/p/${{encodeURIComponent(finalPrompt)}}?model=video&seed=42`;
                document.getElementById("result").innerHTML = `<video src="${{v}}" controls autoplay loop style="width:100%; border-radius:15px;"></video><br><a href="${{v}}" download style="color:#38bdf8; display:block; margin-top:10px;">Yuklab olish</a>`;
            }}
        </script>
    </body>
    </html>
    """
