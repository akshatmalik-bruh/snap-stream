from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from script import subtitleextractor
from fastapi import Form
from fastapi.responses import JSONResponse
from script2 import textgenerator

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(
        request=request, name="item.html"
    )
@app.post("/submit", response_class=HTMLResponse)
async def handle_form(request: Request, youtube_link: str = Form(...)):
    index = youtube_link.find("?v=")
    if(index == -1):
            index = youtube_link.find("be/") + 3
            urlid = youtube_link[index : ]
    else:
        
        index = index + 3
        lastindex = youtube_link.find("&list")
        if(lastindex == -1):
            urlid = youtube_link[index : ]
        else:
         urlid = youtube_link[index : lastindex]
   
    bozo = textgenerator(urlid) 
    things_to_remove = ["\xa0\n", "\xa0\xa0"]
    cleaned_lines = []

    for line in bozo:
        for thing in things_to_remove:
            line = line.replace(thing, " ")
        cleaned_lines.append(line)

   
   
    return templates.TemplateResponse("suibtitle.html", {
        "request": request,
        "List" : bozo
        
    })
   
    