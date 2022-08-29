from fastapi import FastAPI
import uvicorn
import os
import pathlib

from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from src.const import config_map, resource_map
from src.const.global_map import CONFIG_SET, CONFIG_MAP, RESOURCE_MAP
from src.api_endpoint import add_api

os.chdir(pathlib.Path(__file__).parent)

if __name__ == "__main__":
    
    config_map.load_all_config("dev",CONFIG_MAP)
    resource_map.load_all_resource(CONFIG_MAP, RESOURCE_MAP)
    add_api.add_api()
    app= RESOURCE_MAP["fastapi_app"]
    app.mount("/static", StaticFiles(directory="static"), name="static")
    uvicorn.run(app, host="0.0.0.0", port= 8000, debug= True )