while True:
    print("1.celsius to fahrenheit")
    print("2.fahrenheit to celsius")
    print("3.exit")
    
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        C = float(input("Enter temperature in Celsius: "))
        F = C * (9/5) + 32
        print(f"The temperature in Fahrenheit is: {F}")
    elif choice == 2:
        F = float(input("Enter temperature in Fahrenheit: "))
        C = (F - 32) * (5/9)
        print(f"The temperature in Celsius is: {C}")
    elif choice == 3:
        print("Exiting the program.")
        break
    else:
        print("Choice not in the list please enter 1, 2 or 3.")
