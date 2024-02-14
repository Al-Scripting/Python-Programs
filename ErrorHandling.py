# 100862739 Muqshith Shifan ErrorHandling.py
from Lab5_Error_Handling import BankAccount


if __name__ == '__main__':
    #create a bank account
    print("Creating a bank account:")
    bank_account = BankAccount(100)

    #attmept to get the average transaction
    print("\nCreating the bank account")

    print("\nGetting the average transaction (first time)")
    try:
        print(bank_account.get_avg_transaction())
    except AssertionError:
        print("Error: no transaction have been made")
    except:
        print("YOU HAVE DONE SOMETHING WRONG; YOU SHOULD NOT BE SEEING THIS!!!")

    print("\nDepositing Money")
    #attempt to deposit a negative number
    try:
        print(bank_account.deposit(-100))
    except ValueError:
        print("Error: Amount must be greater than zero.")
    except:
        print("YOU HAVE DONE SOMETHING WRONG; YOU SHOULD NOT BE SEEING THIS!!!")

    print("\nDepositing money")
    # attempt to deposit a non-integer
    try:
        print(bank_account.deposit("100"))
    except TypeError:
        print("You must enter a number.")
    except:
        print("YOU HAVE DONE SOMETHING WRONG; YOU SHOULD NOT BE SEEING THIS!!!")

    print("\nWithdrawing money")
    # attempt to withdraw a non-integer
    try:
        print(bank_account.withdraw("100"))
    except TypeError:
        print("You must enter a number.")
    except:
        print("YOU HAVE DONE SOMETHING WRONG; YOU SHOULD NOT BE SEEING THIS!!!")


    print("\nWithdrawing money")
    # attempt to withdraw a negative amount
    try:
        print(bank_account.withdraw(-1000))
    except ValueError:
        print("Amount must be greater than zero.")
    except:
        print("YOU HAVE DONE SOMETHING WRONG; YOU SHOULD NOT BE SEEING THIS!!!")



    print("\nWithdrawing money")
    # attempt to withdraw a greater amount than the balance of the account
    try:
        print(bank_account.withdraw(500))
    except ValueError:
        print("Error: Amount cannot be greater than balance.")
    except:
        print("YOU HAVE DONE SOMETHING WRONG; YOU SHOULD NOT BE SEEING THIS!!!")

    # Shows the entering the correct amount works as expected
    bank_account.deposit(200)
    bank_account.withdraw(100)

    #prints the results
    print("\nGetting the average transactions (second time)")
    print(f"\nAverage Transactions: {bank_account.get_avg_transaction()}")
    print(f"Balance: {bank_account.get_balance()}")

