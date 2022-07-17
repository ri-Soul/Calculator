from math import *
import operator
import operators_
import random

print("\nBASIC: *, /, -, +\n\n")
print("LCM: Least Common Multiple (of num1 & num2)\nGCD: Greatest Common Divisor (of num1 & num2)\n\n")
print("RAND: RANDom (between num1 & num2)\n\n")
print("DIVIDING:\nMOD: the rest (of num1)\"num2\n\n")
print("POWERS:\nSQRT: squareroot (of num1)\nPOWER: (num1 to) the power (of num2)\n\n")
print("FREQUENTION-TABLE:\nAF>RF: Absolute Frequention(num1) --> Relative Frequention\nRF>AF: Relative Frequention --> Absolute Frequention\nRF>CA: Relative Frequention --> Center Angle\nCA>RF: Center Angle --> Relative Frequention\n\n")

num1 = float(input("Enter num1: "))
print("IF IS NOT NEEDED: ENTER")
num2 = float(input("Enter num2: "))
print("IF IS NOT NEEDED: ENTER")
num3 = float(input("Enter num3: "))

Operator = input("Enter operator: ")

Operators = {"*":operator.mul,
"/":operator.div,
"-":operator.sub,
"+":operator.add,

"LCM":operators_.LCM
"GCD":operators_.GCD

"RAND":random.randint

"MOD":operator.mod

"SQRT":operators_.SQRT
"POWER":operator.pow,

"AF>RF":operators_.AF_RF
"RF>AF":operators_.RF_AF
"RF>CA":operators_.RF_CA
"CA>RF":operators_.CA_RF
}

debug = Operators.get(Operator, "Invalid operator!")
print(debug(num1, num2, num3))
