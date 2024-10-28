from math import trunc

from fastapi import FastAPI

app = FastAPI()

@app.get("/", description="This is our first route.", deprecated=True)
async def base_get_route():
    return {"message": "Hello World"}

@app.post("/")
async def post():
    return {"message": "Hello From the Post Route"}

@app.put("/")
async def put():
    return {"message": "Hello From the Put Route"}