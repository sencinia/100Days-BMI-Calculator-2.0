# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = weight / (height**2)

if bmi < 18.5:\
  print(f"Your BMI is {int(bmi)}, you are underweight.")
elif bmi > 18.5 and bmi < 25:
  print(f"Your BMI is {int(bmi)}, you have a normal weight.")
elif bmi > 25 and bmi < 30:
  print(f"Your BMI is {int(bmi)}, you slightly overweight.")
elif bmi > 30 and bmi < 35:
  print(f"Your BMI is {int(bmi)}, you are obese.")
else:
  print(f"Your BMI is {int(bmi)}, you are clinically obese.")




