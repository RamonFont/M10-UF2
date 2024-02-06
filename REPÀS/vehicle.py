import json

class Vehicle:
    def __init__(self, make, model, year, color, mileage, fuel_type):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = mileage
        self.fuel_type = fuel_type

    # Getters
    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_color(self):
        return self.color

    def get_mileage(self):
        return self.mileage

    def get_fuel_type(self):
        return self.fuel_type

    # Setters
    def set_make(self, make):
        self.make = make

    def set_model(self, model):
        self.model = model

    def set_year(self, year):
        self.year = year

    def set_color(self, color):
        self.color = color

    def set_mileage(self, mileage):
        self.mileage = mileage

    def set_fuel_type(self, fuel_type):
        self.fuel_type = fuel_type

    # Mostrar las partes del vehículo
    def show_parts(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")
        print(f"Mileage: {self.mileage}")
        print(f"Fuel Type: {self.fuel_type}")

    # Convertir el objeto a un diccionario
    def to_dict(self):
        return {
            "make": self.make,
            "model": self.model,
            "year": self.year,
            "color": self.color,
            "mileage": self.mileage,
            "fuel_type": self.fuel_type
        }

if __name__ == "__main__":
    # Crear objeto
    my_vehicle = Vehicle("Toyota", "Camry", 2022, "Azul", 15000, "Gasolina")

    # Mostrar las partes del vehículo
    my_vehicle.show_parts()

    # Convertir el objeto a un diccionario y mostrarlo en formato JSON
    vehicle_dict = my_vehicle.to_dict()
    print("Vehicle as JSON:")
    print(json.dumps(vehicle_dict, indent=2))
