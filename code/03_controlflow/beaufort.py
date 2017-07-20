speed = int(input("Enter the speed of wind in knots\n"))

if speed < 1:
    print("Calm")
elif 1 <= speed <= 3:
    print("Light air")
elif 4 <= speed <= 27:
    print("Breeze")
elif 28 <= speed <= 47:
    print("Gales")
elif 48 <= speed <= 63:
    print("Storm")
else:
    print("Hurricane")
