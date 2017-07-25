i = 1
days = int(input("Enter number of days in month"))
start = int(input("Enter day of the month"))

while i <= days:
    # print("hello", end="")
    print("%3d" % (i), end="")
    if(i == 7 or i == 14 or i == 21 or i == 28):
        print("\n")
    i += 1
