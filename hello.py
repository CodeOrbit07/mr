print("1-addition")
print("2-substraction")
print("3-multiplicatiion")
print("4-division")

option=int(input("choose an operation "))

if(option in [1,2,3,4]):
    num1=int(input("enter number 1  "))
    num2=int(input("enter number 2  "))
    if(option == 1):
        result=num1+num2
    elif(option==2):
        result =num1-num2
    elif(option==3):
        result=num1*num2
    elif(option==4):
        result=num1//num2
else:
    print("error 😡😡😡 enter num between 1 to 4")

print("result =  "  + str(result))
        
        


        


    