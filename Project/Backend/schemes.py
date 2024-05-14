from pydantic import BaseModel

class UserResponse(BaseModel):
    """
    Model for user response after registration or login.
    """
    username: str
    profile_pic: str
    class Config:
        orm_mode = True