
# OBJECT = A "bundle" of related attributes {variables} and methods (functions)
#          Example: phone(is_on = True), cup(liquid = "coffee"), book(pages = 310)
#          You need a "class" to create many objets

# class = (blueprint) used to design the structure and layout of an object


from object_oriented_car_example import Car

car1 = Car("Mercedes", 1999, "blue", False)
car2 = Car("Mustang", 2015, "white", True)
car3 = Car("Porsche", 2026, "silver", True)

#print(car1.model, car1.year, car1.color, car1.for_sale)
#print(car2.model, car2.year, car2.color, car2.for_sale)
#print(car3.model, car3.year, car3.color, car3.for_sale)

#car1.drive()
#car3.stop()

car1.describe()



