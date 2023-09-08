''' You are painting a wall the instruction on the paint can says that 1 can of paint can cover 5 square  meter
  of wall given a random height and width of wall calculate how many cans of paint you will need to buy. '''

# height = int(input("enter the height of the wall:  "))
# width = int(input("enter the width of the wall in meter: "))
# coverage = 5
# total_no_of_can = (height * width)/coverage
# print(total_no_of_can)

import math 

def paint_calc(height, width, cover ):
  area = height * width
  num_of_cans = math.ceil(area / cover)
  print(f"you will need {num_of_cans} cans of paint ")

test_h = int(input("height of the wall "))
test_w = int(input("width of wall "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)