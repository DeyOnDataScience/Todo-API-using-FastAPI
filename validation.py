from pydantic import BaseModel

class TodoCreate(BaseModel):
    title: str
    description: str
class TodoUpdate(BaseModel):
    id: int | None=None
    title: str | None=None
    description: str | None=None

class TodoResponse(BaseModel):
    id: int
    title: str
    description: str

    class Config:
        orm_mode = True