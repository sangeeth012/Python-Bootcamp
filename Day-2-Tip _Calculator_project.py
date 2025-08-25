print(" Welcome to the tip calculator ")
user_bill_amount = float(input(" What was the total bill amount: $"))
user_tip_amount = int(input(" Who much tip did yu like to give ? 10 12 $ 15! ?"))
user_spilt_bill = int(input(" How many people to spilt the bill: ?"))
tip_percentage = (user_bill_amount *user_tip_amount) /100
spilt_amount = (tip_percentage + user_bill_amount) / user_spilt_bill
final_amount  = round(spilt_amount,2)
print(f"your final bill amount for each person: {final_amount}")