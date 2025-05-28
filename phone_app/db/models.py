from .database import Base
from sqlalchemy import String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from fastapi import Depends, HTTPException
from datetime import datetime
from passlib.hash import bcrypt


class UserProfile(Base):
    __tablename__ = 'user_profile'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)

    def set_passwords(self, password: str):
        self.hashed_password = bcrypt.hash(password)

    def check_password(self, password: str):
        return bcrypt.verify(password, self.hashed_password)


class RefreshToken(Base):
    __tablename__ = 'refresh_token'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    token: Mapped[str] = mapped_column(String, nullable=False)
    created_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    user_id: Mapped[int] = mapped_column(ForeignKey('user_profile.id'))
    user: Mapped['UserProfile'] = relationship('UserProfile')


class Phone(Base):
    __tablename__ = 'phone'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    rating: Mapped[int] = mapped_column(Integer)
    num_ratings: Mapped[int] = mapped_column(Integer)
    ram: Mapped[int] = mapped_column(Integer)
    rom: Mapped[int] = mapped_column(Integer)
    battery: Mapped[int] = mapped_column(Integer)
    front_camera: Mapped[int] = mapped_column(Integer)
