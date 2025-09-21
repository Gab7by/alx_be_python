size = int(input("Enter the size of the pattern: "))
if size > 0:
    row = 0
    while row < size:
        for col in range(size):
            print("*", end="")
        print()  
        row += 1
else:
    print("Please enter a positive integer.")
