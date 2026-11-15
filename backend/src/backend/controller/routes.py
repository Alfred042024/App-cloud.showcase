from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from backend.service.url_crud import *

from backend.models.urls_models import ADD_URLS_TYPE

router_urls = APIRouter()

@router_urls.get("/", response_class=HTMLResponse)
def welcome():
    return '''<h1> Welcome to the API Level </h1>'''

@router_urls.get("/healthz")
def statusrouter_urls():
    return {"status": "OK"} 

@router_urls.get("/api/getInitialApi")
def apiServiceSimpleGET():
    return get_url()

@router_urls.get("/api/getInitialApi/{id}")
def controller_get_url_by_id(id): 
    return get_url_by_id(id)

@router_urls.post("/api/addnewurl")
def add_new_url_controller(body:ADD_URLS_TYPE)  : 
    return add_new_url(body)
    