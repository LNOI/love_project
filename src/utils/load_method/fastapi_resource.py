from fastapi import FastAPI
from src.utils.load_method.load_utils import register_load_method
from src.utils.load_method.common_resource import load_json
from sqlalchemy.engine import Engine
from sqlalchemy import create_engine
import redis

@register_load_method
def fastapi_app() -> FastAPI:
    return FastAPI(title="Fashion Server Ai Nhu",
                description="FastAPI Server for BE",
                version= "1.0.0"
                )
    
@register_load_method
def db_engine(credential_path: str) -> Engine:
    """
    Create database engine

    Args:
        credential_path (str): relative path to credential file

    Returns:
        Engine: sqlalchemy engine
    """

    args = load_json(credential_path)

    username, password, host, port, dbname = args["username"], args["password"], args["host"], args["port"], args["dbname"]
    connection_string = f"postgresql://{username}:{password}@{host}:{port}/{dbname}"
    timeout_config_string = f"-c statement_timeout={args['statement_timeout']}s"
    engine = create_engine(connection_string, pool_size=50, max_overflow=120,
                           connect_args={"options": timeout_config_string})

    return engine


@register_load_method
def redis_connection(host:str, port:int) -> redis.Redis:
    return redis.Redis(host=host, port=port)