from fastapi import FastAPI
import uvicorn
from phone_app.endpoints.api import auth, profile, phone


phone_app = FastAPI(title='Mobile Phone')
phone_app.include_router(auth.auth_router)
phone_app.include_router(profile.user_router)
phone_app.include_router(phone.phone_router)


if __name__ == '__main__':
    uvicorn.run(phone_app, host='0.0.0.0', port=8000)
