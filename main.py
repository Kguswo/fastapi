from enum import Enum

from math import trunc
from pyexpat.errors import messages

from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Optional

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


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items")
async def list_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip:skip + limit]

@app.get("/items/{item_id}")
async def get_item(item_id: str, sample_query_param: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id, "sample_query_param": sample_query_param}
    if q:
        item.update({"q": q})
    if short:
        item.update(
            {
            "description": "Lor em ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse efficitur."
            }
        )
    return item

@app.get("/users/{user_id}/items/{item_id}")
async def get_user_item(user_id: int, item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse efficitur."
            }
        )
    return item

class Item(BaseModel):
    name: str
    description: str | None = None
    price: int
    tax: float | None = None

@app.post("/items")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price * item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

@app.put("/items/{item_id}")
async def create_item_with_put(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result

@app.get("/items2")
async def read_items(
        q: str
           | None = Query(
            ...,
            min_length=3,
            max_length=10,
            regex="^[a-zA-Z]*$",
            title="Sample Query String",
            description="This is a sample query string",
            deprecated=True,
            alias="item-query"
            )
        ):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}, {"item_id": "Baz"}]}
    if q:
        results.update({"q": q})
    return results

@app.get("/items2/hidden")
async def hidden_query_route(hidden_query: str | None = Query(None, include_in_schema=False)):
    if hidden_query:
        return {"hidden_query": hidden_query}
    return {"hidden_query": "Not Found"}