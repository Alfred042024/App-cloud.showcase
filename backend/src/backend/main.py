
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app =  FastAPI()

@app.get("/", response_class=HTMLResponse)
def welcome():
    return '''<h1> Welcome to the API Level </h1>'''

@app.get("/healthz")
def statusApp():
    return {"status": "OK"} 

@app.get("/api/getInitialApi")
def apiServiceSimpleGET():
    return [ 
        {"id": 1, "code": "abc123", "url": "/pagina-uno", "createdAt": "2026-11-01T10:00:00Z", "clicks": 4},
        {"id": 2, "code": "xyz789", "url": "/pagina-due", "createdAt": "2026-11-03T15:30:00Z", "clicks": 0}, 
        {"id": 3, "code": "qwe456", "url": "/pagina-tre", "createdAt": "2026-11-05T09:15:00Z", "clicks": 12}
        ]