class MoneyNotEnoughError(Exception):
    pass

class PINCodeError(Exception):
    pass

class UnderageTransactionError(Exception):
    pass

class MoneyIsNegativeError(Exception):
    pass

pin, amount, age = [int(x) for x in input().split(', ')]

while True:
    command = input()
    if command == "End":
        break
    parts = command.split('#')
    if parts[0] == "Send Money":
        money_to_send = float(parts[1])
        pin_code = int(parts[2])
        if money_to_send > amount:
            raise MoneyNotEnoughError("Insufficient funds for the requested transaction")
        if pin_code != pin:
            raise PINCodeError("Invalid PIN code")
        if age < 18:
            raise UnderageTransactionError("You must be 18 years or older to perform online transactions")
        else:
            amount -= money_to_send
            print(f"Successfully sent {money_to_send:.2f} money to a friend")
            print(f"There is {amount:.2f} money left in the bank account")

    if parts[0] == "Receive Money":
        money_received = int(parts[1])
        if money_received < 0:
            raise MoneyIsNegativeError("The amount of money cannot be a negative number")
        else:
            amount += money_received / 2
            print(f"{money_received / 2:.2f} money went straight into the bank account")