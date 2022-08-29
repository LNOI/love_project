from fastapi import FastAPI
from src.utils.load_method.load_utils import register_load_method

@register_load_method
def fastapi_app() -> FastAPI:
    return FastAPI(title="Fashion Server Ai Nhu",
                description="FastAPI Server for BE",
                version= "1.0.0"
                )
    
