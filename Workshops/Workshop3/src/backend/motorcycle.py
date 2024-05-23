from Workshops.Workshop3.src.backend.vehicles import Vehicles
from Workshops.Workshop3.src.backend.engine import Engine
class Motorcycle(Vehicles):
  def __init__(self, chasis: str, model: int, year: int, engine: 'Engine', handling: str):
        super().__init__(chasis, model, year, engine)
        self.handling = handling