
def pin_code(pin):
    if pin=='1234':
        return True
    else:
        return False


def withdrawal():
    balance=100
    cash= int(input("Pleae enter the amount you would like to withdraw?"))
    if cash <= balance:
        balance = balance-cash
        print('you now have {} in your account'.format(balance))
        return True
    else:
        print('you do not have enough money in your account')
        return False


def log():
    chances=0
    while chances <3:
        pin=input("Pleae enter your pin code?")
        if pin_code(pin):
            print('correct PIN')
            withdrawal()
            return True
        else:
            print('incorrect pin')
            chances+=1
    print("Too many incorrect pin entered, the card is now blocked")
    return False

def menu():
    print('Welcome to atm')
    log()
menu()






