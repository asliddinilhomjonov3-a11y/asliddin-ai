@app.get("/")
async def home(request: Request):
    # Bu usul eng to'g'ri va xatoliksiz usul
    return templates.TemplateResponse("index.html", {"request": request})
