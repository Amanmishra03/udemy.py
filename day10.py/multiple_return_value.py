def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return(f"{formated_f_name} {formated_l_name} ")
    print("Aman is agood boy. ")
print(format_name("ANGELA","angela"))
''' Here aman is a good boy is not printed because no any command is executed after return command
 coputer understand that return is the last command from the code so he ignore all command after return.'''



def format_name(f_name, l_name):
    # if f_name == "" or l_name == "":
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return(f"result: {formated_f_name} {formated_l_name} ")
print(format_name(input("What is your first name ? "),
input("What is your last name ? ")))




def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return(f"result: {formated_f_name} {formated_l_name} ")
print(format_name(input("What is your first name ? "),
input("What is your last name ? ")))





def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid input. "
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return(f"result: {formated_f_name} {formated_l_name} ")
print(format_name(input("What is your first name ? "),
input("What is your last name ? ")))

