import factorial

try:
    number=-1
    result=factorial.factorial(number)

    print(f"{number}! = {result}")
except TypeError as et:
    print("Type Error: ",et)
except ValueError as ev:
    print("Value Error: ",ev)
