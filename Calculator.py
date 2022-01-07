num1 = input("Enter num1: ")
num2 = input("Enter num2: ")
Operator = input("Enter operator * or / or - or +: ")

def calculate():
  if Operator == "*":
    return float(num1) * float(num2)
  elif Operator == "/":
     return float(num1) / float(num2)
  elif Operator == "+":
    return float(num1) + float(num2)
  else:
    return float(num1) - float(num2)

result = calculate()
print(result)