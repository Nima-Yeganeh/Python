class Car:
    """Just a simple program that written for cars"""
    def __init__(self,make_and_model,year,gearbox):
        """Initialize make_and_model ,year ,gearbox"""
        self.make_and_model = make_and_model
    def drive(self):
        print(f"{self.make_and_model} {self.year} {self.gearbox} is now driving")

    def stop_driving(self):
        print(f"{self.make_and_model} {self.year} {self.gearbox} is STOPPED !")
    