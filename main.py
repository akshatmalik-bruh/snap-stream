from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from script import subtitleextractor
from fastapi import Form

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(
        request=request, name="item.html"
    )
@app.post("/submit", response_class=HTMLResponse)
def handle_form(request: Request, youtube_link: str = Form(...)):
    subtitleextractor(youtube_link)  

   
    return templates.TemplateResponse("item.html", {
        "request": request
        
    })