from src.const.global_map import RESOURCE_MAP
import logging
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from src.utils.basemodel import account_schemas as Schemas
logger = logging.getLogger('app_logger')
app = RESOURCE_MAP["fastapi_app"]
from src.const.global_map import RESOURCE_MAP 
from fastapi.responses import RedirectResponse
import uuid
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home(request: Request):
    return RedirectResponse("/login")

@app.get("/login")
async def render_loging(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/login_love")
async def handle_logging( input_map: Schemas.AccountSchemas,request: Request):
    cursor=RESOURCE_MAP["mysql_db"].cursor()
    query =f"select username,password from accounts where username='{input_map.username}' and password = '{input_map.password}'"
    cursor.execute(query)
    myresult= cursor.fetchall()
    if len(myresult) >= 1:
        short_uuid=str(uuid.uuid1())
        query= """
            update accounts
            set uuid = %s
            where username= %s
        """
        cursor.execute(query, (short_uuid, myresult[0][0]))
        RESOURCE_MAP["mysql_db"].commit()
        return {
            "success": True,
            "username": myresult[0][0]
        }
    return {"success": False}

@app.get("/get_chat",response_class = HTMLResponse)
async def page_love(request: Request):
    return templates.TemplateResponse("chat.html", context={"request": request})

@app.get("/love",response_class = HTMLResponse)
async def page_love(request: Request):
    return templates.TemplateResponse("chat.html", context={"request": request})



