from Workshops.Workshop3.src.backend.vehicles import Vehicles
from Workshops.Workshop3.src.backend.engine import Engine
from Workshops.Workshop3.src.backend.car import Car
from Workshops.Workshop3.src.backend.motorcycle import Motorcycle
from Workshops.Workshop3.src.backend.truck import Truck
from Workshops.Workshop3.src.backend.yacht import Yacht
def create_vehicle():
    vehicle_type = input("Enter the type of vehicle (car, truck, yacht, or motorcycle): ")
    chasis = input("Enter the chasis (A or B): ")
    model = input("Enter the model: ")
    year = input("Enter the year: ")
    engine_type = input("Enter the engine type: ")
    potency = int(input("Enter the engine potency: "))
    weight = int(input("Enter the engine weight: "))

    if vehicle_type.lower() == 'car':
        num_doors = int(input("Enter the number of doors: "))
        vehicle = Car(chasis, model, year, Engine(engine_type, potency, weight), num_doors)
    elif vehicle_type.lower() == 'truck':
        num_wheels = int(input("Enter the number of wheels: "))
        vehicle = Truck(chasis, model, year, Engine(engine_type, potency, weight), num_wheels)
    elif vehicle_type.lower() == 'yacht':
        size = int(input("Enter the size of the yacht: "))
        vehicle = Yacht(chasis, model, year, Engine(engine_type, potency, weight), size)
    elif vehicle_type.lower() == 'motorcycle':
        handling = input("Enter the handling type of the motorcycle: ")
        vehicle = Motorcycle(chasis, model, year, Engine(engine_type, potency, weight), handling)
    else:
        print("Invalid vehicle type.")
        return None

    return vehicle

def review_vehicles(vehicles):
    print("Registered vehicles:")
    for idx, vehicle in enumerate(vehicles, start=1):
        print(f"\nVehicle {idx}:")
        print(f"Type: {type(vehicle).__name__}")
        print(f"Chassis: {vehicle.chasis}")
        print(f"Model: {vehicle.model}")
        print(f"Year: {vehicle.year}")
        print(f"Engine Type: {vehicle.engine.tyype}")
        print(f"Engine Potency: {vehicle.engine.potency}")
        print(f"Engine Weight: {vehicle.engine.weight}")
        gas_consumption = vehicle.gas_consumption()
        if gas_consumption is not None:
              print(f"Gas consumption: {gas_consumption}")
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