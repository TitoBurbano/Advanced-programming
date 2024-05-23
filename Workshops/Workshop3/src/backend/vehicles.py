from Workshops.Workshop3.src.backend.engine import Engine
class Vehicles:
  def __init__(self, chasis: str, model: int, year: int, engine: 'Engine'):
    self.chasis= chasis
    self.model= model
    self.year= year
    self.engine = engine
  def gas_consumption(self):
    if self.chasis == 'A' or 'a':
      return 1.1 * self.engine.potency + 0.2 * self.engine.weight - 0.3
    elif self.chasis == 'B' or 'b':
      return 1.1 * self.engine.potency + 0.2 * self.engine.weight - 0.5
    else:
      return None