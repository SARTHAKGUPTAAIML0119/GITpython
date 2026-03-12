import math

def calculate(operation, *args):
    if not args:
        return "No numbers provided"
    
    if operation == "+":
        return sum(args)
    
    elif operation == "-":
    
        first, *rest = args 
        return first - sum(rest)
    
    elif operation == "*":
        result = 1
        for i in args:
            result *= i
        return result
    
    elif operation == "/":
        first, *rest = args
        result = first
        for i in rest:
            if i == 0: return "Zero Error"
            result /= i
        return result
    
    else:
        return "Unknown Operation"
    
print("Here is a basic calculator for you \n enter the operator and numbers below")

op=str(input("Enter the operator :"))
numbers=[]
while True:
    num=input("enter number (Enter done if done)   :")
    if num.lower()=="done":
        break
    else:
        numbers.append(float(num))

print("result:",calculate(op,*numbers))


