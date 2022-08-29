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

@app.post("/create_tables_accounts")
async def create_tables(request: Request):
    cursor=RESOURCE_MAP["mysql_db"].cursor()
    query ="""create table if not exists accounts (
            id int not null primary key auto_increment,
            uuid varchar(1000),
            username varchar(50) not null ,
            password varchar(50) not null)
        """
    cursor.execute(query)
    RESOURCE_MAP["mysql_db"].commit()
    return { "Create Tables ": "Success" }

@app.post("/drop_tables")
async def create_tables(request: Request):
    cursor=RESOURCE_MAP["mysql_db"].cursor()
    query =""" drop tables accounts
        """
    cursor.execute(query)
    RESOURCE_MAP["mysql_db"].commit()
    return { "Insert": "Success" }


@app.post("/insert_account")
async def insert_account(input_map: Schemas.AccountSchemas,request: Request):
    cursor=RESOURCE_MAP["mysql_db"].cursor()
    query ="insert into accounts (username,password) values (%s,%s)"
    cursor.execute(query, (input_map.username,input_map.password))
    RESOURCE_MAP["mysql_db"].commit()
    return { "Insert": "Success" }

