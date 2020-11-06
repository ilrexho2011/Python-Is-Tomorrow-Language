#----------------------------------------------------------------------------------------------------------------------
#                                 Homework #9 (Classes)
#----------------------------------------------------------------------------------------------------------------------
'''
Details:

Create a class called "Vehicle" and methods that allow you to set the "Make", "Model", "Year,", and "Weight".
The class should also contain a "NeedsMaintenance" boolean that defaults to False, and and "TripsSinceMaintenance"
Integer that defaults to 0. Next an inheritance classes from Vehicle called "Cars".
The Cars class should contain a method called "Drive" that sets the state of a boolean isDriving to True.
It should have another method called "Stop" that sets the value of isDriving to false.
Switching isDriving from true to false should increment the "TripsSinceMaintenance" counter.
And when TripsSinceMaintenance exceeds 100, then the NeedsMaintenance boolean should be set to true.
Add a "Repair" method to either class that resets the TripsSinceMaintenance to zero, and NeedsMaintenance to false.
Create 3 different cars, using your Cars class, and drive them all a different number of times. Then print out
their values for Make, Model, Year, Weight, NeedsMaintenance, and TripsSinceMaintenance

Extra Credit:

Create a Planes class that is also an inheritance class from Vehicle. Add methods to the Planes class for Flying
and Landing (similar to Driving and Stopping), but different in one respect: Once the NeedsMaintenance boolean
gets set to true, any attempt at flight should be rejected (return false), and an error message should be printed saying
that the plane can't fly until it's repaired.

'''

class Vehicle():

    def __init__(self, make, model, year, weight, neMa=False, triSi=0):
        self.Make = make
        self.Model = model
        self.Year = year
        self.Weight = weight
        self.NeedsMaintenance = neMa         # NeedsMaintenance
        self.TripsSinceMaintenance = triSi   # TripsSinceMaintenance

class Cars(Vehicle):

    def __init__(self, Make, Model, Year, Weight, NeedsMaintenance, TripsSinceMaintenance, isDrv=False):
        Vehicle.__init__(self, Make, Model, Year, Weight, NeedsMaintenance, TripsSinceMaintenance)
        self.isDriving = isDrv

    def Drive(self):
        self.isDriving = True

    def Stop(self):
        self.isDriving = False
        self.TripsSinceMaintenance += 1
        if self.TripsSinceMaintenance > 100:
            self.NeedsMaintenance = True

    def Repair(self):
        self.TripsSinceMaintenance = 0
        self.NeedsMaintenance = False

    def __str__(self):
        return "The " + self.Model + " " + self.Make + ", built in year " + self.Year + ", weighing " + str(
            self.Weight) + " Kg's, \nUntil now has done " + str(
            self.TripsSinceMaintenance) + " trips since the maintenance.\nNeeds maintenance: " + str(
            self.NeedsMaintenance) + "\n\n"

class Planes(Vehicle):

    def __init__(self, Make, Model, Year, Weight, NeedsMaintenance, TripsSinceMaintenance, isFly=False):
        Vehicle.__init__(self, Make, Model, Year, Weight, NeedsMaintenance, TripsSinceMaintenance)
        self.isFlying = isFly

    def Flying(self):
        if self.NeedsMaintenance == True:
            print("This plane is grounded and it can't take flight until repaired!")
        else:
            self.isFlying = True

    def Landing(self):
        if self.isFlying == True:
            self.isFlying = False
            self.TripsSinceMaintenance += 1
            if self.TripsSinceMaintenance > 100:
                self.NeedsMaintenance = True

    def Repair(self):
        self.TripsSinceMaintenance = 0
        self.NeedsMaintenance = False

Car1 = Cars("Volkswagen", "Passat", "2018", 2139, False, 0)
Car2 = Cars("BMW", "535d", "2019", 2075, False, 0)
Car3 = Cars("Skoda", "Fabia", "2019", 2580, True, 0)

Plane1 = Planes("Tupolev", "184 72", "1972", 8700, False, 0)

for c1 in range(54):
    Car1.Drive()
    Car1.Stop()

for c2 in range(63):
    Car2.Drive()
    Car2.Stop()

for c3 in range(71):
    Car3.Drive()
    Car3.Stop()

print(Car1)

print(Car2)

print(Car3)

# Can use also
# Car1.Repair()
# print(Car1)

for p1 in range(102):
    Plane1.Flying()
    Plane1.Landing()

# Can use also
# Plane1.Repair()
