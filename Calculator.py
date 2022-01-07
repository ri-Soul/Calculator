num1 = input("Enter num1: ")
num2 = input("Enter num2: ")
Operator = float(input("Enter operator * or / or - or +: "))

def calculate():
  if Operator == "*":
    return num1 * num2
  elif Operator == "/":
     return num1 / num2
  elif Operator == "+":
    return num1 + num2
  else:
    return num1 - num2

result = calculate()
print(result)
