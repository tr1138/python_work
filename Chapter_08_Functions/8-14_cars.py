def make_car(make, model, **car_info):
    car_info['make'] = make
    car_info['model'] = model
    return car_info

car = make_car('subaru', 'outback', colour='blue', tow_package=True)
print(car)