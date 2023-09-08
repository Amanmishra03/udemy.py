# To calculate the BMI
# BMI=weight(kg)/height(m)*height(m)
weight=input("Enter your weight in kg ")
height=input("Enter your height in m ")
bmi=int(weight) / float(height)**2
print(bmi)
bmi_as_int=int(bmi)
print(bmi_as_int)