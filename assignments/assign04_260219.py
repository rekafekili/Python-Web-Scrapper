def inputOperation() -> None:
    print("Choose an operation")
    print("\tOptions are: +, -, * or /.")
    print("\tWrite 'exit' to finish.")
    opInput = input()
    if opInput == "+" or opInput == "-" or opInput == "*" or opInput == "/":
        return opInput
    else:
        return "ERR"


def printResult(resultNum) -> None:
    print("Result:", resultNum)


def runCalculater() -> bool:
    augendNum = int(input("Choose a number: "))
    addendNum = int(input("Choose another one: "))
    opInput = inputOperation()
    if opInput == "+":
        printResult(augendNum + addendNum)
        return True
    elif opInput == "-":
        printResult(augendNum - addendNum)
        return True
    elif opInput == "*":
        printResult(augendNum * addendNum)
        return True
    elif opInput == "/":
        printResult(augendNum / addendNum)
        return True
    elif opInput == "exit":
        return False
    else:
        print("Operation Error. Please try again.")
        return False


while True:
    if not runCalculater():
        print("Calculator Finished")
        break
