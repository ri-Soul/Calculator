num1 = float(input("Enter num1: "))
Operator = input("Enter operator *, /, -, +, T(ool): ")
num2 = float(input("Enter num2: "))

def calculate():
  if Operator == "*":
    return num1 * num2
  elif Operator == "/":
     return num1 / num2
  elif Operator == "+":
    return num1 + num2
  elif Operator == "-":
    return num1 - num2
  elif Operator == "T":
    print("LCM: Least Common Multiple\nGCD: Greatest Common Divisor\nMOD: rest\nSQRT: squareroot\nPOWER: to the power of\nABS: absolute")
    print("ROUNDING ROUND: above and 0.5 UP, under 0.5 DOWN\nCEIL:UP\nFLOOR: DOWN")
    print("FREQUENTION-TABLE AF>RF, RF>AF")
    Tool = input("Enter the tool: ")
    if Tool == "LCM":

    elif Tool == "GCD":

    elif Tool == "MOD":

    elif Tool == "SQRT":

    elif Tool == "POWER":

    elif Tool == "ABS":
    
    elif Tool == "ROUND":

    elif Tool == "CEIL":

    elif Tool == "FLOOR":

  else:
    return "Operator doesn't exist"

print(calculate())
