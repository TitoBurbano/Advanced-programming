from fastapi import FastAPI, HTTPException
from .schemes import UserResponse
from .models import User
from .users import Authentication


app = FastAPI()
authentication = Authentication("postgresql://new_user:password@localhost:5432/mydatabase")

@app.post("/sign_in", response_model=UserResponse)
def sign_in(user: User):
    """
    Endpoint para registrar un nuevo usuario.
    """
    try:
        profile = authentication.sign_in(user.username, user.password)
        return {"username": profile.username, "profile_pic": profile.profile_pic}
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

@app.post("/login", response_model=UserResponse)
def login(user: User):
    """
    Endpoint para autenticar un usuario existente.
    """
    try:
        profile = authentication.login(user.username, user.password)
        return {"username": profile.username, "profile_pic": profile.profile_pic}
    except ValueError as ve:
        raise HTTPException(status_code=401, detail=str(ve))
