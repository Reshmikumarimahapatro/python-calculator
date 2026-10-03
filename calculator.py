print("========================")
print("    PYTHON CALCULATOR")
print("========================")

while True:


    choice = input("Calculate or exit? ").lower()
    if choice == "exit":
        break
    num1 = float(input("enter the 1st number"))
    operation = input("enetr your operator(+,-,%,*,^,/): ")
    num2 = float(input("enter the 2nd number"))

    if operation == "+":
        result=num1+num2
        print("Result:", result)
    elif operation == "-":
        result=num1-num2
        print("Result:", result)
    elif operation == "*":
        result=num1*num2
        print("Result:", result)

    elif operation == "%":
        result=num1%num2
        print("Result:", result)

    elif operation == "/":
        if num2 == 0:
            print("cannot divide by zero")
        else:
            result=num1 / num2
            print("Result:", result)

    elif operation == "^":
        print("Result:", result)
        print(num1 ** num2)

    else:
        print("Invalid operator!")

    again = input("do you want to calculate again? (yes or no): ").lower()

    if again == "no":
        break