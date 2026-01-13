def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return int(a/b) ,a%b

op=input("Enter your choice \n(a).Add \n(b).Subtract \n(c).Multiply \n(d).Divide \n")

n1=int(input("Enter a number: "))
n2=int(input("Enter a second number: "))
if op == 'a':
    print(f"Sum of {n1} and {n2} is {add(n1,n2)}")
elif op == 'b':
    print(f"Difference of {n1} and {n2} is {sub(n1,n2)}")
elif op == 'c':
    print(f"Product of {n1} and {n2} is {mul(n1,n2)}")
elif op == 'd':
    print(f"Quetiont and remainder of {n1} and {n2} is {div(n1,n2)}")
else:
    print("Invalid input")




