from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None


@app.put('/items7{item_id}')
async def update_item(
    item_id: int, item: Item, user: User, importance: Annotated[int, Body()]
    ):
    results = {'item_id': item_id, 'item': item, 'user': user, 'importance': importance}
    return results