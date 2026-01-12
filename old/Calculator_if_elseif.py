num1=int(input("Enter the first number:"))
opr=input("Enter the operator '+', '-', '*', '/', '%' you want to perform:")
num2=int((input("Enter the second number:")))
if opr=="+":
    print("The sum of the",num1,"and the",num2,"is:",(num1+num2))
elif opr=="-":
    print("The sub of the",num1,"and the",num2,"is:",(num1-num2))
elif opr=="*":
    print("The mlt of the",num1,"and the",num2,"is:",(num1*num2))
elif opr=="/":
    print("The div of the",num1,"and the",num2,"is:",(num1/num2))
elif opr=="%":
    print("The rem of the",num1,"and the",num2,"is:",(num1%num2))
else:
    print("Wrong Input")
