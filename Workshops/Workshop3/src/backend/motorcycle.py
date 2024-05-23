from vehicles import Vehicles
from engine import Engine
class Motorcycle(Vehicles):
  def __init__(self, chasis: str, model: int, year: int, engine: 'Engine', handling: str):
        super().__init__(chasis, model, year, engine)
        self.handling = handling