from pydantic import BaseModel, Field

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str = Field(..., min_length=1, max_length=64)

class UserResponse(UserBase):
    id: int
    todos: list["TodoResponse"] = []

    class Config:
        orm_mode = True

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
    user_id: int

    class Config:
        orm_mode = True