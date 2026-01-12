while True:
    print("1.area")
    print("2.perimeter")
    print("3.exit")
    
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        A = float(input("Enter length of the rectangle: "))
        B = float(input("Enter breadth of the rectangle: "))
        C = A*B
        print(f"Area of the rectangle is : {C} sq units.")
    elif choice == 2:
        A = float(input("Enter length of the rectangle: "))
        B = float(input("Enter breadth of the rectangle: "))
        C = 2*(A+B)
        print(f"Perimeter of the rectangle is: {C} units.")
    elif choice == 3:
        print("Exiting the program.")
        break
    else:
        print("Choice not in the list please enter 1, 2 or 3.")
