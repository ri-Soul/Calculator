from math import *
import operator
i
num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))
print("\nBASIC: *, /, -, +\n\n")
print("LCM: Least Common Multiple \nGCD: Greatest Common Divisor\n\n")
print("DIVIDING:\nMOD: the rest or quotient\n\n")
print("POWERS:\nSQRT: squareroot\nPOWER: to the power of\n\n")
print("ABS: absolute\n\n")
print("ROUNDING:\nROUND:above and 0.5 UP, under 0.5 DOWN\nCEIL: UP\nFLOOR: DOWN\n\n")
print("FREQUENTION-TABLE:\nAF>RF: Absolute Frequention --> Relative Frequention\nRF>AF: Relative Frequention --> Absolute Frequention\nCA>RF: Center Angle --> Relative Frequention\nRF>CA: Relative Frequention --> Center Angle:\n\n")

Operator = input("Enter operator: ")

Operators = {"*":operator.mul(num1, num2),
"/":operator.div(num1, num2)
"-":operator.sub(num1, num2)
"+":operator.add(num1, num2),

"LCM":
"GCD":

"ABS":operator.abs(), 

}

Debug = Operators.get(Operator, "Invalid operator!")

print(calculate())
