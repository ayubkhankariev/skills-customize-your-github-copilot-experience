from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Optional

app = FastAPI(title="Items API - Starter")


class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None


# In-memory store: item_id -> Item
db: Dict[int, Item] = {}
next_id = 1


@app.get("/items", response_model=list[Item])
def list_items():
    return list(db.values())


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    item = db.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.post("/items", response_model=Item, status_code=201)
def create_item(item: Item):
    global next_id
    # allow client-provided id if positive and unused; otherwise assign one
    if item.id in db or item.id <= 0:
        item.id = next_id
        next_id += 1
    else:
        next_id = max(next_id, item.id + 1)
    db[item.id] = item
    return item


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, payload: Item):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    payload.id = item_id
    db[item_id] = payload
    return payload


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    del db[item_id]
    return None


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("starter-code:app", host="127.0.0.1", port=8000, reload=True)
