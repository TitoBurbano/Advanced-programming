from Workshops.Workshop3.src.backend.vehicles import Vehicles
from Workshops.Workshop3.src.backend.engine import Engine
class Car(Vehicles):
  def __init__(self, chasis: str, model: int, year: int, engine: 'Engine', num_doors: int):
        super().__init__(chasis, model, year, engine)
        self.num_doors = num_doors