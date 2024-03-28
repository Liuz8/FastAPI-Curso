from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field


app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = Field(
        #validaciones adicionales para body
        default=None, title='The description of the item', max_length=300
    )
    price: float = Field(gt=0, description='The price must be grater tha zero')
    tax: float | None = None


@app.put('/item/{item_id}')
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {'item_id': item_id, 'item': item}
    return results