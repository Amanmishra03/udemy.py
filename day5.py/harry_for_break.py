'''if we use break then it stop the loop where we command it 
if we use break to stop loop then else statement can not run 
else statement can run only if loop close or final itself not break by command '''

for i in range(10):
    print(i)
    if i == 5:
        break
else:
    print("the statement is not end naturally so this is not run ")
