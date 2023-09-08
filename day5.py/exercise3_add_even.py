''' To  add Even number between 1 & 100 including 1 & 100 '''
''' AMAN METHOD '''
total_even  = 0
for number in range (1, 101):
    if number % 2 == 0:
        total_even += number
print(total_even)

''' MA'AM METHOD '''
total = 0
for number in range (2,101,2):
    total += number
print(total)