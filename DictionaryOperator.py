import operator
import operators_

Operators = {
    "*":operator.mul,
    "/":operator.div,
    "-":operator.sub,
    "+":operator.add,

    "LCM":operators_.LCM,
    "GCD":operators_.GCD,

    "RAND":random.randint,

    "MOD":operator.mod,

    "SQRT":operators_.SQRT,
    "POWER":operator.pow,

    "AF>RF":operators_.AF_RF,
    "RF>AF":operators_.RF_AF,
    "RF>CA":operators_.RF_CA,
    "CA>RF":operators_.CA_RF
}

while True:
    while True:
        print("\nBASIC: *, /, -, +\n\n")
        print("LCM: Least Common Multiple (of num1 & num2)\nGCD: Greatest Common Divisor (of num1 & num2)\n\n")
        print("RAND: RANDom (between num1 & num2)\n\n")
        print("DIVIDING:\nMOD: the rest (of num1)\"num2\n\n")
        print("POWERS:\nSQRT: squareroot (of num1)\nPOWER: (num1 to) the power (of num2)\n\n")
        print("FREQUENTION-TABLE:\nAF>RF: Absolute Frequention(num1) --> Relative Frequention(num2) AF-total(num3)\nRF>AF: Relative Frequention(num1) --> Absolute Frequention(num2) AF-total(num3)\nRF>CA: Relative Frequention(num1) --> Center Angle(num2)\nCA>RF: Center Angle(num1) --> Relative Frequention(num2)\n\n")

        num1 = float(input("Enter num1: "))
        print("IF IS NOT NEEDED: ENTER")
        num2 = float(input("Enter num2: "))
        print("IF IS NOT NEEDED: ENTER")
        num3 = float(input("Enter num3: "))

        Operator = input("Enter operator: ")

        debug = Operators.get(Operator, "Invalid operator!")

        if Operators.get(Operator, "!") == "!":
            print("Invalid confirmed!")
            break
        if not(len(num1)):
            print("Operator not found...")
            break

        if len(num3):
            print(debug(num1, num2, num3))
        elif len(num2):
            print(debug(num1, num2))
        elif len(num1):
            print(debug(num1))
        else:
            print("No given value to num1...")
            break