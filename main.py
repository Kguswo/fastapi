from enum import Enum

from math import trunc
from pyexpat.errors import messages

from fastapi import FastAPI

app = FastAPI()

@app.get("/", description="This is our first route.", deprecated=False)
async def base_get_route():
    return {"message": "Hello World"}

@app.post("/")
async def post():
    return {"message": "Hello From the Post Route"}

@app.put("/")
async def put():
    return {"message": "Hello From the Put Route"}

@app.get("/users")
async def list_users():
    return {"message": "list users route"}

@app.get("/users/{user_id}")
async def get_user(user_id: str):
    return {"user_id": user_id}

@app.get("/users/me")
async def get_current_user():
    return {"Message": "this is the current user"}

class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"

@app.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.vegetables:
        return {"food_name": food_name,
                "message": "you are healthy"}

    if food_name.value == "fruits":
        return {"food_name": food_name,
                "message": "you are still healthy, but like sweet things"}

    return {"food_name": food_name,
            "message": "you are not healthy"}