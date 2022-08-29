import json
from src.utils.load_method.load_utils import register_load_method
import mysql.connector
import redis
@register_load_method
def mysql_conn( credential_path: str):
    with open(credential_path , "r" ) as f:
        args= json.load(f)
        
    # host,port,database,username,password = args["host"],args["port"],args["database"],args["username"],args["password"]
    
    engine = mysql.connector.connect(**args)
    return engine


@register_load_method
def redis_conn( credential_path: str):
    with open(credential_path , "r" ) as f:
        args= json.load(f)    
    # host,port,database,username,password = args["host"],args["port"],args["database"],args["username"],args["password"]
    engine= redis.Redis(host=args["host"], port=args["port"])
    return engine
    

    


