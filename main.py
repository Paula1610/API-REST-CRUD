from fastapi import FastAPI, HTTPException
from schemas.Item import Item

app = FastAPI(docs_url="/docs", redoc_url=None)

items = []

@app.get("/")
def root():
    return {"Hello": "World"}

@app.get("/items", response_model=list[Item])
def get_items():
    items_active = []
    for item in items:
        if item.active == True:
            items_active.append(item)
    return items_active

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    if (item_id < 0) or item_id >= len(items):
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")
    items[item_id] = item
    return item

@app.post("/items", response_model=Item)
def add_item(item: Item):
    items.append(item)
    return item

@app.delete("/items/{item_id}", response_model=Item)
def delete_item(item_id: int):
    if (item_id < 0) or item_id >= len(items):
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")
    items[item_id].active = False
    return items[item_id]

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    if (item_id < 0) or item_id >= len(items):
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")
    return items[item_id]

