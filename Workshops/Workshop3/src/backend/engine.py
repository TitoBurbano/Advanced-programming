from pydantic import BaseModel
class Engine(BaseModel):
    engine_type: str
    potency: int
    weight: int

