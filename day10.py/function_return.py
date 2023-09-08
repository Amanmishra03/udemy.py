# ''' .title is used to write first letter capital and all small words. '''
# # function with output

# # 1st. TYPE
# def format_name(f_name, l_name):
#     print(f_name.title())
#     print(l_name.title())
# format_name("angela","ANGELA")



# # 2nd. TYPE
# def format_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     print(f"{formated_f_name} {formated_l_name} ")
# format_name("ANGELA","angela")


# # 3rd. TYPE
# def format_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return(f"{formated_f_name} {formated_l_name} ")
# formated_string = format_name("ANGELA","angela")
# print(formated_string)


# # 4th. TYPE
# def format_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return(f"{formated_f_name} {formated_l_name} ")
# print(format_name("ANGELA","angela"))


name = input("Enter your name ").title()
print(name)