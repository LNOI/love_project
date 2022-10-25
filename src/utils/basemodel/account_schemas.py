from pydantic import BaseModel
from typing import Union,Optional

class AccountSchemas(BaseModel):
    username : str
    password : str
    
class StorageMessageSchemas(BaseModel):
    id : int
    
class ResponeSchemas(BaseModel):
    content : Union[str,None]=None
    
    
    
    