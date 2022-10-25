from tkinter.tix import Tree
from src.const.global_map import RESOURCE_MAP
import logging
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from src.utils.query.db_utils import  execute_raw_query
from fastapi.requests import Request
from src.utils.basemodel import account_schemas as Schemas
import random
logger = logging.getLogger('app_logger')
app = RESOURCE_MAP["fastapi_app"]
from src.const.global_map import RESOURCE_MAP 
from fastapi.responses import RedirectResponse

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home(request: Request):
    return RedirectResponse("/login")

@app.get("/login")
async def render_loging(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/login_love")
async def handle_logging( input_map: Schemas.AccountSchemas,request: Request):
    query = """
        select username from users
        where username = :username and password = :password
    """ 
    res = execute_raw_query(raw_query=query, username=input_map.username,password= input_map.password)
    if res :
        return {"success": True}
    return {"success": False}


@app.get("/get_chat",response_class = HTMLResponse)
async def page_love(request: Request):
    return templates.TemplateResponse("chat.html", context={"request": request})


@app.get("/love",response_class = HTMLResponse)
async def page_love(request: Request):
    query = """
        select link,date,content from memory
    """ 
    res = execute_raw_query(raw_query=query)
    
    memory= [{
            'link': r[0] ,
            'date' : r[1],
            'content':r[2],
            'isvideo': True if 'mp4'  in r[0] else False,
            'rotate' : random.randint(-4,4)*5
        }
        for r in res ]
    
    query = """
        select * from storage_mess
    """
    res = execute_raw_query(raw_query=query)
    storage_message = [
        {
            'id' : s[0],
            'sender': s[1],
            'receiver': s[2],
            'thumbnail': s[3],
            'title': s[4],
            'content': s[5],
            'date' : s[6],
            'seen' :  [ 'static/img/thumbnail/thumbnail_anhyeu.jpg' if i==1 else 'static/img/thumbnail/thumbnail_emyeu.jpg' for i in s[7]]  
        }
        for s in res
    ]
    return templates.TemplateResponse("index.html", context={"request": request,'memory':memory,'storage_message': storage_message })

@app.post("/get_one_message")
async def get_one_message(input_map:Schemas.StorageMessageSchemas,request:Request):
    id = input_map.id
    query = """
        select * from storage_mess
        where id=:id
    """
    res = execute_raw_query(raw_query=query,id=id)
    result = {
         'sender': res[0][1],
            'receiver': res[0][2],
            'thumbnail': res[0][3],
            'title': res[0][4],
            'content': res[0][5],
            'date' : res[0][6],
            'seen' :  [ 'static/img/thumbnail/thumbnail_anhyeu.jpg' if i==1 else 'static/img/thumbnail/thumbnail_emyeu.jpg' for i in res[0][7]]  
    }
    return result
    
@app.post("/get_content_main")
async def get_one_message(request:Request):
    query = """
        select * from content_main
        where id=:id
    """
    res = execute_raw_query(raw_query=query,id=1)
    result = {
        "title" :  res[0][1],
        "content" :  ["Love Content 1!","Love Content 2!","Love Content 3!","Love Content 4!","Love Content 5!"]
    }
    return result
    
    
@app.post("/write_accept")
async def get_one_message(input_map: Schemas.ResponeSchemas , request:Request):
    content =  input_map.content
    print(content)
    query = """
        INSERT INTO public.history_response
        ("content")
        VALUES('%s');

    """%(content)
    res = execute_raw_query(raw_query=query)
    return {}
    
