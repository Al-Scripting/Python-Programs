# Muqshith Shifan - ATM - Lab 4 - 2022-10-06
# 100862739
import time

# Sets Gloabal Variables
balance = float(0)
otherBalance = float(0)


# Def for this Program
def getBalance():
    return balance


def getOtherBalance():
    return otherBalance


def printBalances():
    print("Your Balance is $", format(getBalance()))
    print("Your Other Balance is $", format(getOtherBalance()))


def deposit(money):
    balance = getBalance()
    print("Money deposit successful!")
    return balance + money


def withdraw(money):
    balance = getBalance()
    print("Money is withdrawn successfully!")
    return balance - money


def transfer(money):
    balance = getBalance()
    otherBalance = getOtherBalance()
    print("Money has been transferred to Other-Balance!")
    return balance - money, otherBalance + money


# Ask User for name and pin
name = str(input("Enter Username :> "))
pin = str(input("Enter PIN :> "))

while True:
    # Prints The Intro Statement
    print("\nHello ", name, ", Welcome to NoodleBank\n")
    print("\t\t0. Logout and Exit (exit)")
    print("\t\t1. View Account Balance (get Balance)")
    print("\t\t2. View Account Other-Balance (get other balance")
    print("\t\t3. View Account All Account Balances (show balances)")
    print("\t\t4. Deposit Cash (deposit)")
    print("\t\t5. Withdraw Cash (withdrawal)")
    print("\t\t6. Transfer (transfer)")

    userInput = input("\nEnter number or type to proceed > ").strip().lower()

    if userInput == "1" or userInput == "get balance":
        print("\nAccount Balance is: $", str(getBalance()))

    elif userInput == "2" or userInput == "get other balance":
        print("\nOther Account Balance is: $", str(getOtherBalance()))

    elif userInput == "3" or userInput == "show balances":
        printBalances()

    elif userInput == "4" or userInput == "deposit":
        print("\nBalance is $", str(getBalance()))

        money = float(input("How much money do you want to deposit: $"))

        if money < 0:
            print("Insufficient funds! Please enter a valid amount")
        else:
            balance = deposit(money)
    elif userInput == "5" or userInput == "withdrawal":
        print("Your Balance is: $", str(getBalance()))

        money = float(input("How much money do you want to withdraw: $"))

        if money > balance or money < 0:
            print("Insufficient funds! Please enter a valid amount")
        else:
            balance = withdraw(money)

    elif userInput == "6" or userInput == "transfer":
        printBalances()
        money = float(input("how much you want to transfer? $"))

        if money > balance or money < 0:
            print("Insufficient funds! Please enter a valid amount")
        else:
            balance, otherBalance = transfer(money)

    elif userInput == "0" or userInput == "exit" or userInput == "stop" or money == "stop" or money == "exit":
        print("\nThank You For Choosing NoodleBank, Have a Great Day")
        break
    else:
        print("Invalid Option")

# END OF PROGRAM MUQSHITH SHIFAN #100852739
