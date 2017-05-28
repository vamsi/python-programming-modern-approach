revenue = []
while True:
    amount = input("Enter Income")
    if amount == 'q':
        break
    else:
        revenue.append(int(amount))
print(revenue)
if sum(revenue) <= 250000:
    print("No Taxation")
elif 25000 < sum(revenue) < 50000:
    print("10%")
elif 50000 < sum(revenue) < 10000:
    print("20%")
else:
    print("30%")
