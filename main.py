from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import List, Annotated

import models
from database import SessionLocal, engine
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class ChoiceBase(BaseModel):
    choice_text: str
    is_correct: bool

class QuestionBase(BaseModel):
    text: str
    choices: List[ChoiceBase]


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@app.post('/questions/')
async def create_questions(question: QuestionBase, db: db_dependency):
    db_question = models.Question(text=question.text)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    for i in question.choices:
        db_choice = models.Choices(choice_text=i.choice_text, is_correct=i.is_correct)
        db.add(db_choice)
    db.commit()

@app.get('/questions/')
async def get_questions(db: db_dependency):
    return db.query(models.Question).all()


@app.get('/positions/')
async def get_positions(db: db_dependency):
    return db.query(models.Position).all()

class PositionBase(BaseModel):
    title: str
    is_company_related: bool


class BranchGETBase(BaseModel):
    id: int
    title: str
    region: str
    phone: str


class BranchCreateBase(BaseModel):
    title: str
    is_main: bool
    address: str
    region: str
    phone: str



@app.post('/position/create/')
async def create_position(position: PositionBase, db: db_dependency):
    ps = models.Position(title=position.title, is_company_related=position.is_company_related)
    db.add(ps)
    db.commit()
    db.refresh(ps)
    return ps


@app.patch('/position/{id}/')
async def patch_position(id: int, position: PositionBase, db: db_dependency):
    ps = db.query(models.Position).filter(models.Position.id == id).first()
    if ps is None:
        raise HTTPException(status_code=404, detail="Position not found")
    ps.title = position.title
    ps.is_company_related = position.is_company_related
    db.commit()
    db.refresh(ps)
    return ps


@app.delete('/position/{id}/')
async def delete_position(id: int, db: db_dependency):
    ps = db.query(models.Position).filter(models.Position.id == id).first()
    if ps is None:
        raise HTTPException(status_code=404, detail="Position not found")
    db.delete(ps)
    db.commit()
    return


@app.get('/branches/')
async def get_branches(db: Session = Depends(get_db)):
    return db.query(models.Branch).all()


@app.post('/branch/create')
async def create_branches(branch: BranchCreateBase, db: db_dependency):
    item = models.Branch(**branch.dict())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@app.get('/branch/{id}/')
async def detail_branch(id: int, db: db_dependency):
    return db.query(models.Branch).filter(models.Branch.id == id).first()
