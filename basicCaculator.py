def main():
    firstNumber = float(input("What do you want the first number to be? "))
    secondNumber = float(input("What do you want the second number to be? "))
    operator = input("What operation do you want to do? (Ex Add,Addition,+,Plus) ")
    operator = operator.lower()
    calculation(operator, firstNumber, secondNumber)

def calculation(opperand, x, y):
    global t
    if t > 0:
        opperand = input("There must've been a mistake, can you retry again for opperand. ")

    if(opperand == ("add" or "addition" or "+" or "plus")):
        print(x + y)
    elif(opperand == ("subtract" or "subtraction" or "sub" or "-")):
        print(x - y) 
    elif(opperand == ("multiply" or "multiplication" or "multi" or "*")):
        print(x * y)
    elif(opperand == ("divide" or "division" or "div" or "/")):
        print(x / y)
    else:
        t = t + 1
        calculation(opperand, x, y)

t = 0
main()

