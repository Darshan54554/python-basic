num1=float(input("enter your first number:"))
num2=float(input("enter you second number:"))
operation=input("enter your operation(+,-,*,/)")
if operation=="+":
    result=num1+num2
    print(f"the result is:{result}")
elif operation=="-":
    result=num1-num2
    print(f"the result is:{result}")
elif operation=="*":
    result=num1*num2
    print(f"the result is:{result}")
elif operation=="/":
    if num2 != 0:
        result = num1 / num2
        print(f"The result is: {result}")
    else:
        print("Error: Division by zero is not allowed.")

else:
    print("invalid operation! please choose +,-,*,/")    
