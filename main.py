#BMI Calculator
height = input("enter your height in m: ") #string
weight = input("enter your weight in kg: ") #string
w = float(weight)
h = float(height)
BMI = w/(h**2)
print(int(BMI))
