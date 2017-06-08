lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

print("Prime numbers between {} and {} are:".format(lower, upper))

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
