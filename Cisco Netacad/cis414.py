class Vehicle:
    pass

class LandVehicle(Vehicle):
    pass

class TrackedVehicle(LandVehicle):
    pass


myVehicle = Vehicle()
myLandVehicle = LandVehicle()
myTrackedVehicle = TrackedVehicle()

for obj in [myVehicle, myLandVehicle, myTrackedVehicle]:
    for cls in [Vehicle, LandVehicle, TrackedVehicle]:
        print(isinstance(obj, cls), end="\t")
    print()
print(type(myTrackedVehicle).__name__)
print(type(myLandVehicle).__name__)
print(type(myVehicle).__name__)
y=[TrackedVehicle.__bases__,LandVehicle.__bases__,Vehicle.__bases__]
for i in y:
    for j in i:
       print(j.__name__)
