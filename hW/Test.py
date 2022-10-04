class Vehicle:
    def __init__(self, material, wheel):
        self.material = material
        self.wheel = wheel


class Moto(Vehicle):
    def __init__(self, material, wheel, mass):
        super().__init__(material, wheel, mass)
        self.mass = mass

vehicle = Vehicle("Metal", "Pirelli")
print(vehicle.material)
print(vehicle.wheel)
# print(Vihicle.__init__)