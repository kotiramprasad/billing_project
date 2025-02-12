pin=1819
balance=5000
def atm_withdrawl():
    try:
        enter_pin=int(input("enter your pin"))
        if pin!=enter_pin:
            raise ValueError("please enter a correct pin")
        amount=int(input("enter the amount"))
        if amount>balance:
            raise ValueError("insufficent balances")
        if amount<=0:
            raise ValueError("invalid withdrawl amount")
        remining=balance-amount
        print(f"your transaction is successful of amount:{amount}")
        print(f"your remining balanceis:{remining}")

    except ValueError as e:
        print(f"error:{e}")

    except Exception as e:
        print(f"an unexpected error:{e}")

    finally:
        print("thanks for using atm")

atm_withdrawl()