from pydantic import BaseModel
from typing import Union,Optional

class AccountSchemas(BaseModel):
    username : str
    password : str
    
    
    
    