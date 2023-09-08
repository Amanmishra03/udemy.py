''' List is used to store multiple data in a single variable
    List is always used in square brackets and seperated by [,] 
    list is also used to arrange order of the data  
    like no. of state in India [up,bihar,uk,mumbai,etc..] '''   
state_of_India = ["up","bihar","uk","ap","jharkhand","mumbai","delhi","punjab"]
# if we want to print a single data from list then we have to write as
print(state_of_India[2])
print(state_of_India[-2])

#    if we want to change the name of a list then 
state_of_India[1] = "Bihari"
# if we want to add a data in list then we have to use (dot append without space) .append
state_of_India .append("Chandigarh")
state_of_India.extend(["J&k", "kerla", "tamil nadu"])
state_of_India.remove("uk")
print(state_of_India)

state_of_america = ["aman","aman","bb","bb"]
print(state_of_america)

set= {5,4,5}
print(set)


aman = {4,5,3,5,2,1,1}
print(aman)

