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

    def fill_gasoline(self):
        print(f"{self.make_and_model} is on a Gas Station and FILLED GAS ! (GAS : FULL)")

    def show_info(self):
        print(f"\nCAR INFO : {self.make_and_model}\nYEAR : {self.year}\nGEARBOX TYPE : {self.gearbox}")

class ElectricCar(Car):

    def __init__(self, make_and_model, year, gearbox):
        super().__init__(make_and_model, year, gearbox)

    def charge_electric(self):
        print(f"{self.make_and_model} is on a SuperCharge Station and CHARGED with ELECTRICITY ! (BATTERY : 100%)")

my_toyota = Car("Toyota Corolla", "2015","Automatic")
my_toyota.show_info()
my_toyota.drive()
my_toyota.stop_driving()
my_toyota.fill_gasoline()

my_tesla = ElectricCar("Tesla Plaid","2020","Electric Gearbox")
my_tesla.show_info()
my_tesla.drive()
my_tesla.charge_electric()
