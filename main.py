from database import Base,engine,SessionLocal
from model import Todo
from validation import TodoCreate,TodoResponse,TodoUpdate
from sqlalchemy.orm import Session
from fastapi import FastAPI,Depends,HTTPException

Base.metadata.create_all(bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()


@app.post("/todos/",response_model=TodoResponse)
def create_todo(todo: TodoCreate,db: Session=Depends(get_db)):
    new_todo = Todo(title=todo.title,description=todo.description)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo
@app.get("/todos/",response_model=list[TodoResponse])
def get_todos(db: Session=Depends(get_db)):
    return db.query(Todo).all()

@app.put("/todos/{todo_id}", response_model=TodoResponse)
def update_todo(todo_id: int, update_data: TodoUpdate, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    for key, value in update_data.model_dump(exclude_unset=True).items():
        setattr(todo, key, value)

    db.commit()
    db.refresh(todo)
    return todo

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    db.delete(todo)
    db.commit()
    return {"message": f"Todo with ID {todo_id} deleted successfully"}
