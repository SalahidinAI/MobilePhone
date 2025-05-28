from pydantic import BaseModel


class UserProfileListSchema(BaseModel):
    id: int
    username: str
    password: str

    class Config:
        from_attributes = True


class UserProfileSchema(BaseModel):
    username: str
    password: str

    class Config:
        from_attributes = True


class PhoneSchema(BaseModel):
    rating: int
    num_ratings: int
    ram: int
    rom: int
    battery: int
    front_camera: int

    class Config:
        from_attributes = True


class PhoneListSchema(BaseModel):
    id: int
    rating: int
    num_ratings: int
    ram: int
    rom: int
    battery: int
    front_camera: int

    class Config:
        from_attributes = True
