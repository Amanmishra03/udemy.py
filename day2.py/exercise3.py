'''Create the program using f-string that tells us
 how many days, week, month, we  have left 
 if we live until 90 years old'''
# 1 year =365 days, 1 year =52 week, 1 year =12 month

age=int(input("Enter your age "))
years_remaining= 90-age
month_remaining= years_remaining*12
week_remaining= years_remaining*52
days_remaining= years_remaining*365
message=f"i have {years_remaining} years,{month_remaining} month, {week_remaining} week, {days_remaining} days "
print(message)




#  1 year =365 days, 1 year =52 week, 1 year =12 month

age = int(input("Enter your age: "))
year_left = (90 - age)
month_left = (year_left * 12)
week_left = (year_left * 52)
days_left = (year_left * 365)
print(f"you have {year_left} year, {month_left} month left , {week_left} week left , and {days_left} days ")