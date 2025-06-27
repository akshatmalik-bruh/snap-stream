from fastapi import FastAPI, Request,Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from script import subtitleextractor
from fastapi import Form
from fastapi.responses import JSONResponse
from script2 import textgenerator
from database import Base,engine,get_db  
import models
from typing import Annotated,List
from sqlalchemy.orm import Session
from modelresponse import modelanswer
app = FastAPI()
import json
app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")
Base.metadata.create_all(bind=engine)

db_dependency = Annotated[Session,Depends(get_db)]
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(
        request=request, name="item.html"
    )
@app.post("/submit", response_class=HTMLResponse)
async def handle_form(request: Request, db : db_dependency,youtube_link: str = Form(...)):
    
    
    
    
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
    result = db.query(models.url).filter(models.url.url_link == urlid).first()
    if(result == None):
        
   
        bozo = textgenerator(urlid) 
        things_to_remove = ["\xa0\n", "\xa0\xa0"]
        cleaned_lines = []

        for line in bozo:
            for thing in things_to_remove:
                line = line.replace(thing, " ")
            cleaned_lines.append(line)
        db_url = models.url(url_link = urlid,subtitles = cleaned_lines)
        db.add(db_url)
        db.commit()
        db.refresh(db_url)
        response = modelanswer(db_url.subtitles)
        finalresponse = response.replace("json","")
        clean_response = response.strip().removeprefix("```json").removeprefix("json").removesuffix("```").strip()
        data = json.loads(clean_response)
        
        
      
        return templates.TemplateResponse("subtitle.html", {
        "request": request,
        "List" : data,
        "concepts": data["concepts"]
        
        })
    else:
        response = modelanswer(result.subtitles)
        finalresponse = response.replace("json","")
        clean_response = response.strip().removeprefix("```json").removeprefix("json").removesuffix("```").strip()
        data = json.loads(clean_response)
        
        
        return templates.TemplateResponse("subtitle.html",{
            "request" : request,
            "List" : data,
            "concepts": data["concepts"]
        })
   
    