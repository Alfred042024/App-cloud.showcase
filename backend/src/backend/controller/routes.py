from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from backend.service.url_crud import *

from backend.models.urls_models import ADD_URLS_TYPE

router_urls = APIRouter(prefix="/api")

@router_urls.get("/", response_class=HTMLResponse)
def welcome():
    return '''<h1> Welcome to the API Level </h1>'''

@router_urls.get("/healthz")
def statusrouter_urls():
    return {"status": "OK"} 

@router_urls.get("/getInitialApi")
def apiServiceSimpleGET():
    return get_url()

@router_urls.get("/getInitialApi/{id}")
def controller_get_url_by_id(id:int): 
    return get_url_by_id(id)

@router_urls.post("/addNewUrl", status_code=201)
def add_new_url_controller(body:ADD_URLS_TYPE)  : 
    return add_new_url(body)

@router_urls.delete("/deleteUrl/{id}",  status_code=204) 
def delete_url_controller(id:int):
    return  delete_url_service(id)
    