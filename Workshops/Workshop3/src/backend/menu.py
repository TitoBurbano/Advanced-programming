from engine import Engine
from car import Car
from motorcycle import Motorcycle
from truck import Truck
from yacht import Yacht

def create_engine():
    engine_type = input("Enter the engine type: ")
    potency = int(input("Enter the engine potency: "))
    weight = int(input("Enter the engine weight: "))
    return Engine(engine_type, potency, weight)

def create_vehicle():
    vehicle_type = input("Enter the type of vehicle (car, truck, yacht, motorcycle), or 'engine' to create only an engine: ")
    if vehicle_type.lower() == 'engine':
        return create_engine()
    
    chasis = input("Enter the chasis (A or B): ")
    model = input("Enter the model: ")
    year = input("Enter the year: ")
    engine = create_engine()

    if vehicle_type.lower() == 'car':
        num_doors = int(input("Enter the number of doors: "))
        vehicle = Car(chasis, model, year, engine, num_doors)
    elif vehicle_type.lower() == 'truck':
        num_wheels = int(input("Enter the number of wheels: "))
        vehicle = Truck(chasis, model, year, engine, num_wheels)
    elif vehicle_type.lower() == 'yacht':
        size = int(input("Enter the size of the yacht: "))
        vehicle = Yacht(chasis, model, year, engine, size)
    elif vehicle_type.lower() == 'motorcycle':
        handling = input("Enter the handling type of the motorcycle: ")
        vehicle = Motorcycle(chasis, model, year, engine, handling)
    else:
        print("Invalid vehicle type.")
        return None

    return vehicle

def review_vehicles(vehicles):
    print("Registered vehicles and engines:")
    for idx, item in enumerate(vehicles, start=1):
        print(f"\nItem {idx}:")
        if isinstance(item, Engine):
            print(f"Type: Engine")
            print(f"Engine Type: {item.tyype}")
            print(f"Engine Potency: {item.potency}")
            print(f"Engine Weight: {item.weight}")
        else:
            vehicle = item
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
        print("2. Create a new engine")
        print("3. Review registered vehicles and engines")
        print("4. Exit")

        option = input("Select an option: ")

        if option == '1':
            new_vehicle = create_vehicle()
            if new_vehicle:
                vehicles.append(new_vehicle)
                print("Vehicle created successfully.")
        elif option == '2':
            new_engine = create_engine()
            if new_engine:
                vehicles.append(new_engine)
                print("Engine created successfully.")
        elif option == '3':
            review_vehicles(vehicles)
        elif option == '4':
            print("Exiting the program...")
            break
        else:
            print("Invalid option. Please select a valid option.")

if __name__ == "__main__":
    menu()