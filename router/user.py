from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from router.schemas import UserRequestSchema, UserResponseSchema
from db.database import get_db
from db import db_user
from typing import List

router = APIRouter(
    prefix='/api/users',
    tags=['users']
)


@router.post('', response_model=UserResponseSchema)
def create(request: UserRequestSchema, db: Session = Depends(get_db)):
    return db_user.create(db, request)


@router.get('/feed', response_model=List[UserResponseSchema])
def feed_initial_articles(db: Session = Depends(get_db)):
    return db_user.db_feed(db)


@router.get('/all', response_model=List[UserResponseSchema])
def get_all_articles(db: Session = Depends(get_db)):
    return db_user.get_all(db)

