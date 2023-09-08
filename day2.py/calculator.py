# print("Welcome to the tip calculator. ")
# bill = float(input("What was the total bill ? "))
# tip = int(input("What percentage tip would you like to give ? 10, 12, or 15 ? "))
# friends = int(input("In how many people bill is divide ? "))
# tips = tip/100
# bills = bill*tips
# total_bill = bills + bill
# final_bills = total_bill / friends
# print(final_bills)



''' BEST WAY TO SOLVE. '''

print("Welcome to the tip calculator. ")
bill = float(input("What was the total bill ? "))
tip = int(input("What percentage tip would you like to give ? 10, 12, or 15 ? "))
friends = int(input("In how many people bill is divide ? "))
bill_with_tip = tip/100 * bill + bill
# bill_with_tip = bill * (1 + tip/100)
total_bill = bill_with_tip / friends
# for round at two decimal point
final_amount = round(total_bill,2)
print(f"Every person should pay {final_amount} ")


