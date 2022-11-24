# ussd
class Calc:
    def sum(self, x, y):
        print(f"The sum of{x} and {y} is {x+y}")

    def sub(self, x, y):
        print(f"The difference between {x} and {y} is {x-y}")

    def div(self, x, y):
        print(f"The division of {x} by {y} is {x/y}")


    def mult(self, x, y):
        print(f"The multiplication of {x} by {y} is {x * y}")

    def sqroo(self, x):
        print(f"The square-root of {x} is {x**0.5}")

    def Gen(self, x, y, z):
        print(f"Your answer is equals to {((-b+((b**2) - (4*a*c)**0.5))/(2*a))} "
              f"or {((-b-((b**2) - (4*a*c)**0.5))/(2*a))}")

calc = Calc()

entry = input(
    "1 for addition\n"
    "2 for subtraction\n"
    "3 for division\n"
    "4 for multiplication\n"
    "5 for square-root\n"
    "6 for general formula\n"
    "Select an operation: "
)

if entry == "1":
     a = int(input("Enter 1st Number: "))
     b = int(input("Enter 2nd Number: "))
     calc.sum(a,b)
elif entry == "2":
    a = int(input("Enter 1st Number: "))
    b = int(input("Enter 2nd Number: "))
    calc.sub(a,b)
elif entry == "3":
    a = int(input("Enter 1st Number: "))
    b = int(input("Enter 2nd Number: "))
    calc.div(a,b)
elif entry == "4":
    a = int(input("Enter 1st Number: "))
    b = int(input("Enter 2nd Number: "))
    calc.mult(a,b)
elif entry == "5":
    a = int(input("Enter your Number: "))
    calc.sqroo(a)
elif entry == "6":
    a = int(input("Enter 1st Number: "))
    b = int(input("Enter 2nd Number: "))
    c = int(input("Enter 3rd Number: "))
    calc.Gen(a,b,c)

else:
    print("Invalid Operation")






