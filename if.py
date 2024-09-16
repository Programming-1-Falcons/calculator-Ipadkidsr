while True:
    sym = input("What should the math symbol be? +,-,*,/,**")
    num1 = float(input("What should the first number you are using be?"))
    num2 = float(input("What should the second number be?"))
    if sym == "+":
        print(num1, "+", num2, "=", num1+num2)

    elif sym == "-":
        print(num1, "-", num2, "=", num1-num2)

    elif sym == "*":
        print(num1, "*", num2, "=", num1*num2)


    elif sym == "/":
        if num2 == 0:
            print ("You can divide by  0")
            continue
        print(num1, "/", num2, "=", num1/num2)

    elif sym == "**":
        print(num1, "**", num2, "=", num1**num2)

    else:
        print("Please type in a valide symbol")