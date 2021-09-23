
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))


BMI = round(weight/(height ** 2), 2)

print(f"\nYour Body Mass Index is  {BMI}\n")

if BMI < 18.5:
  print(f"Your Body Weight is Underweight with {BMI} BMI.")
elif BMI < 25:
  print(f"Your have a normal weight with {BMI} BMI.")
elif BMI < 30:
  print(f"Your BMI indicates you are overweight with {BMI} BMI.")
elif BMI < 35:
  print(f"Your BMI indicates you are obese  with {BMI} BMI.")
else:
  print(f"Your BMI indicates you are cliniically obese with {BMI} BMI.")

