from typing import Annotated

from fastapi import FastAPI, Query

from pydantic import Required

app = FastAPI()


@app.get('/items')
async def read_items(q: Annotated[str | None, Query(min_length=3)] = Required):
    results = {
        'items': [
            {'item_id': 'Foo'},
            {'item_id': 'Bar'}
        ]
    }

    if q:
        results.update({'q': q})

    return results