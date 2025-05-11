print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_amount= tip/100
bill_with_tip= bill*tip_amount
total_bill= bill + bill_with_tip
pay_bill= total_bill/people
round(pay_bill, 2)
print(f"every person shoould pay ${pay_bill}")
