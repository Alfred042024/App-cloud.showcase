from pydantic import BaseModel

class  ADD_URLS_TYPE(BaseModel) : 
    short_url:str
    original_url:str