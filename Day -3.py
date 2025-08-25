print("Welcome to the tip calculator! ")

user_bill_amount = float(input("What was the total bill amount $"))

user_tip_amount =int(input("how much tip did you like to give ? 10 12 or 15!?"))

user_split_bill = int(input("how many people to split the bill ?"))

tip_percentage = (user_bill_amount * user_tip_amount) /100

split_amount = ((tip_percentage + user_bill_amount) / user_split_bill)

final_amount = round(split_amount,2)

print(user_bill_amount)

print(user_tip_amount)

print(user_split_bill)

print(f"your final bill amount for each person: {final_amount}")