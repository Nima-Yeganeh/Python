def get_car_info(car_maker,car_model, car_year):
    """Return a full car info"""
    car_info = f"\nCAR INFO : {car_maker.upper()} {car_model.title()} {car_year}"
    return car_info

bmw = get_car_info("BMW","528i",2016)
myvolvo = get_car_info("Volvo","S40",2008)
vw_car = get_car_info("VW","Golf 7", 2014)
print(bmw)
print(f"My volvo is best {myvolvo}")
print(f"VW is the best {vw_car}")
