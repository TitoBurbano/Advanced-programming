from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

vehicles = []

@app.post("/create-engine/")
async def create_engine(engine: Engine):
    vehicles.append(engine)
    return {"message": "Engine created successfully"}

@app.post("/create-vehicle/")
async def create_vehicle(vehicle: Vehicle):
    vehicles.append(vehicle)
    return {"message": "Vehicle created successfully"}

@app.get("/review-vehicles/")
async def review_vehicles():
    return {"vehicles": vehicles}

@app.get("/review-engines/")
async def review_engines():
    engine_list = [vehicle for vehicle in vehicles if isinstance(vehicle, Engine)]
    return {"engines": engine_list}


