import time

class Vehicle:
    def changedirection(left, on):
        if on:
          print("start turning the vehcile")
        else:
          print("stop turning vehcile")

    def turn(left):
        left.changedirection(True)
        time.sleep(2)
        left.changedirection(False)

class TrackedVehicle(Vehicle):
    def controltrack(left, stop):
        if stop:
          print("start turning the trackedvehcile")
        else:
          print("stop turning trackedvehcile")

    def changedirection(left, on):
        left.controltrack(on)

class WheeledVehicle(Vehicle):
    def turnfrontwheels(left, on):
        if on:
          print("start turning the wheeledvehcile")
        else:
          print("stop turning the wheeledvehcile")

    def changedirection(left, on):
        left.turnfrontwheels(on)

obj1=Vehicle()
obj2=TrackedVehicle()
obj3=WheeledVehicle()
#obj1.turn()
obj2.turn()
#obj3.turn()