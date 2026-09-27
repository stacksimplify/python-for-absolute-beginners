"""
Workshop Problem-04: variables and naming (Car Spec Card) (solution)

Concepts: variables, print(), the sep option, naming rules and conventions.
"""

"""
Problem-1:
  Write a program that stores a car's brand ("Toyota"), model ("Camry"), and year (2021)
  in variables, then prints a spec card: the title "Car Spec Card", each labeled detail
  on its own line, and finally the brand and model on one line joined by " - ".

Expected output:
Car Spec Card
Brand: Toyota
Model: Camry
Year: 2021
Toyota - Camry
"""
# Problem-1 Task-1: store car details, print spec card
brand = "Toyota"
model = "Camry"
year = 2021

print("Car Spec Card")
print("Brand:", brand)
print("Model:", model)
print("Year:", year)

print(brand, model, sep=" - ")

"""
Problem-2:
  Write a program that stores a car_brand ("Toyota") and model_year (2021) in snake_case
  variables and a MAX_SPEED (180) as an UPPER_CASE constant, then prints all three.

Expected output:
Toyota
2021
180
"""
# Problem-2 Task-1: snake_case vars and UPPER_CASE constant, print all three
car_brand = "Toyota"
model_year = 2021
MAX_SPEED = 180

print(car_brand)
print(model_year)
print(MAX_SPEED)
