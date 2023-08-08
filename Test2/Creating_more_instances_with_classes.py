class Car:
    """Just a simple program that written for cars"""
    def __init__(self,make_and_model,year,gearbox):
        """Initialize make_and_model ,year ,gearbox"""
        self.make_and_model = make_and_model
        self.year = year
        self.gearbox = gearbox
    def drive(self):
        print(f"{self.make_and_model} {self.year} {self.gearbox} is now driving")

    def stop_driving(self):
        print(f"{self.make_and_model} {self.year} {self.gearbox} is STOPPED !")

    def start_drifting(self):
        print(f"{self.make_and_model} {self.year} {self.gearbox} is DDDDRRRRRRRIFFFFFTTTTINGGG !!!")

my_bmw = Car('BMW 325i','2002','AUTOMATIC')
my_honda = Car('Honda Civic','2015','MANUAL')

print(f"My car's make and model is {my_bmw.make_and_model}")
print(f"My car's year of production is {my_bmw.year}")
print(f"My car's gearbox type is {my_bmw.gearbox}")

my_bmw.drive()
my_bmw.stop_driving()
my_bmw.drive()
my_honda.start_drifting()
my_bmw.drive()
my_bmw.start_drifting()

print(f"My car's make and model is {my_honda.make_and_model}")
print(f"My car's year of production is {my_honda.year}")
print(f"My car's gearbox type is {my_honda.gearbox}")

my_honda.drive()
my_honda.start_drifting()
