'''Write a program to greet all the person names stored in a list l1 and which start with s  '''
l1 = ["harry", "sohan", "sachin", "rahul"]
# for l1 in range (0,4):
#     if (l1[0]) == "s":
#      print("hemlo")
# # if l1[0] == "s":
#     # print(" hemlo")
#     else:
#      print("hii")


for name in l1:
    if name[0] == "s":
        print("hello "+ name)
    else:
     print(name)