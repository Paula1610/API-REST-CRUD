from pydantic import BaseModel

class Item(BaseModel):
    text: str
    active: bool = True