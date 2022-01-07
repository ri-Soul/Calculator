num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))
Operator = input("Enter operator * or / or - o +: ")

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
