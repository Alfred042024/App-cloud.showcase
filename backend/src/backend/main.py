
from fastapi import FastAPI 


app =  FastAPI()

@app.get("/")
def welcome():
    return {"status": "Welcome to the API Level"} 

@app.get("/healthz")
def statusApp():
    return {"status": "OK"} 

@app.get("/api/getInitialApi")
def apiServiceSimpleGET():
    return {
            "_id": "6af0a7ec9b18f769ab3d0ee0",
            "index": 0,
            "guid": "5ed46246-adfe-46ba-96f9-ca5468329f8a",
            "isActive": False,
            "balance": "$2,419.29",
            "picture": "http://placehold.it/32x32",
            "age": 28,
            "eyeColor": "blue",
            "name": "Mable Ryan",
            "gender": "female",
            "company": "CYTREX",
            "email": "mableryan@cytrex.com",
            "phone": "+1 (861) 441-3875",
            "address": "588 Cass Place, Elbert, Arkansas, 9913",
            "registered": "2024-02-28T01:59:36 -01:00",
            "latitude": -86.060727,
            "longitude": -145.68367
        }