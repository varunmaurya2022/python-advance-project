class BalanceException(Exception):
    pass
def checkbalance():
    money=12000
    withdraw=1000
    try:
        balance=money-withdraw
        if (balance<=2000):
          
            raise BalanceException("Insufficient Balance")
        print(balance)
    except BalanceException as be:
        print(be)       
checkbalance()