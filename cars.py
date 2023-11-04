from carfuncs.carcontroll import Car

car1 = Car('Dodge', 'Viper', 1992, 290)
print(car1.brand, end=' ')
print(car1.model)
car1.accelerate()
car1.brake()
car1.display_speed()
print('\n')

car2 = Car('Volkswagen', 'Golf 7 GTi', 2017, 275)
print(car2.brand, end=' ')
print(car2.model)
car2.accelerate()
car2.brake()
car2.display_speed()
