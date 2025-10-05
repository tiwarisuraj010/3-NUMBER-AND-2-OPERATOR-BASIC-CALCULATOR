print(" ==Basic Calculator==")
while True:
    num1=int(input("Enter Number: "))
    num2=int(input("Enter Number: "))
    num3=int(input("Enter Number: "))
    op1=input(" Put(+,-,*,/,): ")
    op2=input(" Put(+,-,*,/,): ")

    if   op1=="+":
        result= num1 + num2
    elif op1=="-":
        result= num1 - num2
    elif op1=="*":
        result= num1 * num2
    elif op1=="/":
        if num2!=0:
            result= num1 / num2
        else:
            print("error:cannot be divided by zero")
            continue
    else:
        print("ERROR")
        continue

    if   op2=="+":
        result += num3
    elif op2=="-":
        result -= num3
    elif op2=="*":
        result *= num3
    elif op2=="/":
        if num3!=0:
            result= result / num3
        else:
            print("error:cannot be divided by zero")
            continue
    else:
        print("Error")
        continue
    print("Result: ", result)
        
        
