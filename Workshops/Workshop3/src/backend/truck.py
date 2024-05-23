from vehicles import Vehicles
from engine import Engine
class Truck(Vehicles):
  def __init__(self, chasis: str, model: int, year: int, engine: 'Engine', num_wheels: int):
        super().__init__(chasis, model, year, engine)
        self.num_wheels = num_wheels