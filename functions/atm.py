balance = 0


def deposit(amount):
    global balance
    balance += amount
    return balance


def withdraw(amount):
    global balance
    balance -= amount
    return balance
