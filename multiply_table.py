def multi_table(num, till=10):
    for i in range(1, till + 1):
        print(f"{num} x {i} = {num * i}")
num = int(input("Enter a number: "))
multi_table(num)
