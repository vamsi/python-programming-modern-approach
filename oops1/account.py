class BankAccount(object):

    num_accounts = 0

    def __init__(obj, name, balance):
        obj.name = name
        obj.balance = balance
        BankAccount.num_accounts += 1

    def del_account(obj):
        BankAccount.num_accounts -= 1

    def deposit(obj, amt):
        obj.balance = obj.balance + amt

    def withdraw(obj, amt):
        obj.balance = obj.balance - amt

    def inquiry(obj):
        return obj.balance
