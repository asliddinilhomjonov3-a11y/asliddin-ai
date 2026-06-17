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
        <input type="text" id="prompt" value="a futuristic city">
        <button onclick="createArt()">Yaratish</button>
        <div id="result" style="margin-top:20px;"></div>
        
        <script>
            function createArt() {
                const resEl = document.getElementById("result");
                const prompt = document.getElementById("prompt").value;
                const url = `https://pollinations.ai/p/${encodeURIComponent(prompt)}?width=512&height=512&seed=1`;
                
                resEl.innerHTML = "Rasmni yuklayapman: <br> " + url + "<br><br>" + 
                                  `<img src="${url}" onerror="this.onerror=null; this.src='https://placehold.co/200x200?text=Xato!';" style="border: 2px solid red;">`;
            }
        </script>
    </body>
    </html>
    """
