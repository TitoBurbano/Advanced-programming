from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .users import Authentication
from typing import List
from .users import MusicInteraction
from .users import Profile
from typing import Union
from .users import SocialInteraction
# Inicializa la clase Authentication con la URL de la base de datos
auth = Authentication(db_url="postgresql://postgres:postgres@localhost:5432/project_db")
music_interaction = MusicInteraction(db_url="postgresql://postgres:postgres@localhost:5432/project_db")
social_interaction = SocialInteraction()

app = FastAPI()


class User(BaseModel):
    username: str
    password: str

# Definición de endpoints
@app.post("/signup/")
def sign_up(username: str, password: str, name: str, age: int):
    try:
        authentication.sign_up(username, password, name, age)
        return {"message": "User signed up successfully"}
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

@app.post("/login/")
def login(user: User):
    try:
        logged_in_user = auth.login(user.username, user.password)
        return logged_in_user
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))


@app.get("/search/")
def search_songs(keyword: str) -> List[Song]:
    return music_interaction.search(keyword)

@app.post("/playlist/create/")
def create_playlist(playlist_name: str) -> Playlist:
    return music_interaction.create_playlist(playlist_name)

@app.post("/suggestions/")
def receive_suggestions(liked_songs: List[Song]) -> List[Song]:
    return music_interaction.receive_suggestions(liked_songs)

@app.post("/like/{song_id}")
def like_song(song_id: int):
    music_interaction.give_like(song_id)
    return {"message": "Song liked successfully"}

@app.post("/customize/")
def customize_profile(username: str, new_password: str = None, new_name: str = None, new_age: int = None, new_profile_pic: str = None):
    try:
        profile = Profile(username=username)
        profile.customize_profile(new_password=new_password, new_name=new_name, new_age=new_age, new_profile_pic=new_profile_pic)
        return {"message": "Profile customized successfully"}
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    
@app.post("/manage_friends/{user_id}/{friend_id}/{action}")
async def manage_friends(user_id: int, friend_id: int, action: str):
    try:
        social_interaction.manage_friends(user_id, friend_id, action)
        return {"message": "Friend action successful"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/follow/{user_id}/{entity_id}/{entity_type}")
async def follow(user_id: int, entity_id: int, entity_type: str):
    try:
        social_interaction.follow(user_id, entity_id, entity_type)
        return {"message": "Follow successful"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/share/{user_id}/{entity_id}/{entity_type}")
async def share(user_id: int, entity_id: int, entity_type: str, song_id: int = None, playlist_id: int = None):
    try:
        social_interaction.share(user_id, entity_id, entity_type, song_id, playlist_id)
        return {"message": "Share successful"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
