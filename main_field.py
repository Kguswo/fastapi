from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

app = FastAPI()

"""
Part 8 -> Body - Fields
"""


class Item(BaseModel):
    name: str
    description: str | None = Field(
        None, title="The description of the item", max_length=300
    )
    price: float = Field(..., gt=0, description="The price must be greater than zero")
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(..., embed=True)):
    results = {"item_id": item_id, "item": item}
    return results
