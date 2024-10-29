from fastapi import FastAPI, Body
from pydantic import BaseModel, HttpUrl

app = FastAPI()

"""
Part 9 -> Body - Nested Models
"""


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: str | None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    image: Image | None = None


class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[Item]


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results


@app.put("/offers")
async def create_offer(offer: Offer = Body(..., embed=True)):
    return offer


@app.pose("images/multiple")
async def create_multiple_images(images: list[Image]):
    return images


@app.post("/blah")
async def create_some_blahs(blahs: dict[int, float]):
    return blahs
