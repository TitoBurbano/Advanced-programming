from pydantic import BaseModel
from engine import Engine
class Vehicle(BaseModel):
    chasis: str
    model: str
    year: int
    engine: Engine
def gas_consumption(self):
    if self.chasis == 'A' or 'a':
      return 1.1 * self.engine.potency + 0.2 * self.engine.weight - 0.3
    elif self.chasis == 'B' or 'b':
      return 1.1 * self.engine.potency + 0.2 * self.engine.weight - 0.5
    else:
      return None