from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session


app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class ChoiceBase(BaseModel):
    choice_text:str
    is_correct:bool

class QuestionBase(BaseModel):
    question_text:str
    choices: List[ChoiceBase]
    
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

# GET by ID
@app.get("/question/{question_id}")
async def read_question(question_id: int, db:db_dependency):
    result = db.query(models.Questions).filter(models.Questions.id == question_id).first()
    if not result:
        raise HTTPException(status_code=404,  detail='Question is not found')
    return result    

# GET Chioce by ID
@app.get("/chioces/{question_id}")
async def read_choices(question_id: int, db:db_dependency):
    result = db.query(models.Choices).filter(models.Choices.question_id == question_id).all()
    if not result:
        raise HTTPException(status_code=404,  detail='Choices is not found')
    return result                     

# POST
@app.post("/question")
async def create_question(question: QuestionBase, db: db_dependency):
    db_question = models.Questions(question_text = question.question_text)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    for chioce in question.choices:
        db_chioce = models.Choices(choice_text = chioce.choice_text,is_correct=chioce.is_correct,question_id=db_question.id)
        db.add(db_chioce)
    db.commit()