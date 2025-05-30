from fastapi import APIRouter, Depends, HTTPException
from phone_app.db.models import Base, UserProfile
from phone_app.db.database import SessionLocal
from phone_app.db.schema import UserProfileSchema, UserProfileListSchema
from sqlalchemy.orm import Session
from typing import List


user_router = APIRouter(prefix='/user', tags=['User Profile'])


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@user_router.get('/', response_model=List[UserProfileListSchema])
async def user_list(db: Session = Depends(get_db)):
    return db.query(UserProfile).all()


@user_router.get('/{user_id}/', response_model=UserProfileSchema)
async def user_detail(user_id: int, db: Session = Depends(get_db)):
    user_db = db.query(UserProfile).filter(UserProfile.id == user_id).first()
    if not user_db:
        raise HTTPException(status_code=404, detail='User not found')
    return user_db


@user_router.put('/{user_id}/', response_model=UserProfileSchema)
async def user_update(user_id: int, user: UserProfileSchema, db: Session = Depends(get_db)):
    user_db = db.query(UserProfile).filter(UserProfile.id == user_id).first()
    if not user_db:
        raise HTTPException(status_code=404, detail='User not found')

    for user_key, user_value in user.dict().items():
        setattr(user_db, user_key, user_value)

    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db


@user_router.delete('/{user_id}/')
async def user_delete(user_id: int, db: Session = Depends(get_db)):
    user_db = db.query(UserProfile).filter(UserProfile.id == user_id).first()
    if not user_db:
        raise HTTPException(status_code=404, detail='User not found')

    db.delete(user_db)
    db.commit()
    return {'message': 'Deleted'}
