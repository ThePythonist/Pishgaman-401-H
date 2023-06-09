class SedanCar:
    def __init__(self, hp, color, fuel, gb):
        self.horsepower = hp
        self.color = color
        self.fuel = fuel
        self.gearbox = gb
        self.rpm = 0

    def car_break(self):
        print("Brrrreeeak!")

    def car_horn(self):
        print("Biiiiiiiiiiiiiib!")

    def accelerate(self, value=0):
        for i in range(value):
            self.rpm += 1000

        print(f"Current round per motor is {self.rpm}")


samand = SedanCar(113, "white", "petrol", "manual")
dena = SedanCar(113, "black", "petrol", "automatic")
i8 = SedanCar(184, "silver", "petrol", "automatic")
x390 = SedanCar(247, "silver", "electricity", "automatic")

# print(samand.horsepower)
# print(i8.horsepower)
# dena.car_break()
# x390.car_horn()
i8.accelerate(6)
