class Vehicle:
    def __init__(self,type):
        self.type=type
    
    def fuel_effc(self,effc):
        print("The fuel efficiency for {0} type is {1}".format(self.type,effc))

class Bike(Vehicle):
    def __init__(self,type,effc):
        super().__init__(type)

    def fuel_effc(self,effc):
        print("Bike is starting.....")
        super().fuel_effc(effc)

bike=Bike("Bike",25)
Vehicle.fuel_effc(bike,30)