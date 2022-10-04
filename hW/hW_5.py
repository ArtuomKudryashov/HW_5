class Vehicle:
    def __init__(self, material, wheel):
        self.material = material
        self.wheel = wheel


    def prototуpe (self):
        return "Excellent model"
    def country(self):
        return "Made  in Spain"

vehicle = Vehicle("Metal", "Pirelli")
print(vehicle.material)
print(vehicle.wheel)
print(vehicle.prototуpe())
print(vehicle.country())
print(vehicle.prototуpe())

print("<<<<<<<<<<<<<<<<<<<<<<<Suzuki>>>>>>>>>>>>>>>>>>>>>>>")
class Moto(Vehicle):
    def __init__(self, material, wheel, mass):
        super().__init__(material, wheel)
        self.mass = mass
    def country(self):
        return "Made  in Japan"

suzuki = Moto('Carbon','Continental','500')
print(suzuki.wheel)
print(suzuki.mass)
print(suzuki.material)
print(suzuki.prototуpe())
print(suzuki.country())
# print(Suzuki.__init__)

print("<<<<<<<<<<<<<<<<<<<<<<<Trek>>>>>>>>>>>>>>>>>>>>>>>")

class Bike (Vehicle):
    def __init__(self, material, wheel, model):
        super().__init__(material,wheel)
        self.model = model

    def country(self):
        return "Made  in the  USA"

trek=Bike('Aluminium', 'Michelin','Trek')
print(trek.material)
print(trek.wheel)
print(trek.model)
print(trek.country())
print(trek.prototуpe())
print(trek.material)

print("<<<<<<<<<<<<<<<<<<<<<<<RoadBike>>>>>>>>>>>>>>>>>>>>>>>")

class RoadBike(Bike):
    def __init__(self,material,wheel,model,type):
        super().__init__(material,wheel,model)
        self.type=type

    def country(self):
       return "Made  in  China"

trek=RoadBike("Carbon","Goodyear","Trek ",'RoadBike')
print(trek.type)
print(trek.model)
print(trek.wheel)
print(trek.material)
print(trek.prototуpe())
print(trek.country())
