from vehicles import Vehicles
from engine import Engine
class Yacht(Vehicles):
  def __init__(self, chasis: str, model: int, year: int, engine: 'Engine', size: int):
        super().__init__(chasis, model, year, engine)
        self.size = size