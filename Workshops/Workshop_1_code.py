"""
This file contains the set of classes necessary to address the problem of the first workshop

Author: Tito Burbano P. - Mar13/24
"""

#====================== Class Engine =====================================================================================
class Engine:
  """This class represents the behavior of a vehicle engine."""    
  def __init__(self, tyype: str, potency: int, weight: float):
    self.tyype = tyype
    self.potency = potency
    self.weight = weight

#====================== Class Vehicle =====================================================================================    
class Vehicles:
  """
  This class represents the behavior of an abstract class
  to define vehicles.
  """
  def __init__(self, chasis: str, model: int, year: int, engine: 'Engine'):
    self.chasis = chasis
    self.model = model
    self.year = year
    self.engine = engine
    self.gas_consumption = None
 
  def calculate_consumption(self):
    """ This method is used to calcualte the vehicle's gas consumption."""
    consumption = ((1.1 * self.engine.potency) + (0.2 * self.engine.weight) - (0.3 if self.chasis == "A" else 0.5))
    self.gas_consumption = consumption

#====================== Class Car ========================================================================================= 
class Car(Vehicles):
  """This class is used to represent a car."""
  def __init__(self, chasis: str, model: int, year: int, engine: 'Engine', num_doors: int):
        super().__init__(chasis, model, year, engine)
        self.num_doors = num_doors


#====================== Class Truck ========================================================================================
class Truck(Vehicles):
  """This class is used to represent a Truck."""
  def __init__(self, chasis: str, model: int, year: int, engine: 'Engine', num_wheels: int):
        super().__init__(chasis, model, year, engine)
        self.num_wheels = num_wheels

#====================== Class Yacht =========================================================================================
class Yacht(Vehicles):
  """This class is used to represent a Yacht."""
  def __init__(self, chasis: str, model: int, year: int, engine: 'Engine', size: int):
        super().__init__(chasis, model, year, engine)
        self.size = size

#====================== Class Motorcycle =====================================================================================
class Motorcycle(Vehicles):
  """This class is used to represent a Motorcycle."""
  def __init__(self, chasis: str, model: int, year: int, engine: 'Engine', handling: str):
        super().__init__(chasis, model, year, engine)
        self.handling = handling
#====================== Menu =================================================================================================        
def create_vehicle():
    print("\nCreating a new vehicle:")
    valid_types = ['car', 'truck', 'yacht', 'motorcycle']
    while True:
        vehicle_type = input("Enter vehicle type (Car/Truck/Yacht/Motorcycle): ").lower()
        if vehicle_type in valid_types:
            break
        else:
            print("Invalid vehicle type. Please enter a valid type.")

    model = input("Enter model: ")
    year = input("Enter year: ")

    valid_chassis = ['A', 'B']
    chasis = input("Enter chassis number (A/B): ").upper()
    while chasis not in valid_chassis:
        print("Invalid chassis type. Please enter 'A' or 'B'.")
        chasis = input("Enter chassis number (A/B): ").upper()

    engine_type = input("Enter engine type: ")
    engine_potency = float(input("Enter engine potency: "))
    engine_weight = float(input("Enter engine weight: "))

    if vehicle_type == 'car':
        num_doors = input("Enter number of doors: ")
        return Car(chasis, model, year, Engine(engine_type, engine_potency, engine_weight), num_doors)
    elif vehicle_type == 'truck':
        num_wheels = input("Enter number of wheels: ")
        return Truck(chasis, model, year, Engine(engine_type, engine_potency, engine_weight), num_wheels)
    elif vehicle_type == 'yacht':
        size = input("Enter size: ")
        return Yacht(chasis, model, year, Engine(engine_type, engine_potency, engine_weight), size)
    elif vehicle_type == 'motorcycle':
        handling = input("Enter handling: ")
        return Motorcycle(chasis, model, year, Engine(engine_type, engine_potency, engine_weight), handling)

def review_vehicles(vehicles):
    print("Registered vehicles:")
    for idx, vehicle in enumerate(vehicles, start=1):
        print(f"\nVehicle {idx}:")
        print(f"Type: {type(vehicle).__name__}")
        print(f"Chasis: {vehicle.chasis}")
        print(f"Model: {vehicle.model}")
        print(f"Year: {vehicle.year}")
        print(f"Engine Type: {vehicle.engine.tyype}")
        print(f"Engine Potency: {vehicle.engine.potency}")
        print(f"Engine Weight: {vehicle.engine.weight}")
        vehicle.calculate_consumption()
        if vehicle.gas_consumption is not None:
            print(f"Gas consumption: {vehicle.gas_consumption}")
        else:
            print("Gas consumption: Not available")
        if isinstance(vehicle, Car):
            print(f"Number of Doors: {vehicle.num_doors}")
        elif isinstance(vehicle, Truck):
            print(f"Number of Wheels: {vehicle.num_wheels}")
        elif isinstance(vehicle, Yacht):
            print(f"Size: {vehicle.size}")
        elif isinstance(vehicle, Motorcycle):
            print(f"Handling: {vehicle.handling}")

def menu():
    vehicles = []

    while True:
        print("\nMenu:")
        print("1. Create a new vehicle")
        print("2. Review registered vehicles")
        print("3. Exit")

        option = input("Select an option: ")

        if option == '1':
            new_vehicle = create_vehicle()
            if new_vehicle:
                vehicles.append(new_vehicle)
                print("Vehicle created successfully.")
        elif option == '2':
            review_vehicles(vehicles)
        elif option == '3':
            print("Exiting the program...")
            break
        else:
            print("Invalid option. Please select a valid option.")

if __name__ == "__main__":
    menu()


    

