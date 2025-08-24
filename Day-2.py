print("**********************")
print("BMI CALCULATOR")
print("Getting data from the user")

# Convert inputs to float for decimal values
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your body weight in kg: "))

# BMI Formula
bmi = weight / (height ** 2)

# Display results
print("\nYour BMI (rounded):", round(bmi, 2))

# Interpretation
if bmi < 18.5:
    print("Category: Underweight")
elif 18.5 <= bmi < 24.9:
    print("Category: Normal weight")
elif 25 <= bmi < 29.9:
    print("Category: Overweight")
else:
    print("Category: Obese")
