from calc import Simplemath,Polycalc

def demo_simplemath():
    print("arithmetic calculator")
    a=float(input("enter a:"))
    b=float(input("enter b:"))
    c=float(input("enter c:"))

    solve=Simplemath(a, b, c)

    while True:
        print("1:addition")
        print("2:substraction")
        print("3:multiplication")
        print("4:division")
        print("5:exit")
        
        option=input("enter option:")

        if option=="1":
              print("sum:",solve.addition())
        elif option=="2":
            print("difference:",solve.substraction())
        elif option=="3":
            print("product:",solve.multiplication())
        elif option=="4":
            print("quotient:",solve.division())
        elif option=="5":
            print("exiting...")
            break
        else:
            print("invalid option!")

def demo_polycalc():
    print("quadratic solver")
    a=int(input("Enter coefficient a: "))
    b=int(input("Enter coefficient b: "))
    c=int(input("Enter coefficient c: "))

    quad=Polycalc(a,b,c)
    quad.roots()

        
while True:
    print("choose an option:")
    print("1:simple math calculator ")
    print("2:quadratic equation solver")
    print("3:exit")

    choice=input("Enter choice:")

    if choice=="1":
        demo_simplemath()
    elif choice=="2":
        demo_polycalc()
    elif choice=="3":
        print("exiting...")
        break
    else:
        print("Invalid choice!")







