from unittest import TestCase

def pin_code(pin):
    if pin=='1234':
        return True
    else:
        return False


def withdrawal(cash):
    balance=100
    cash= int(input("Pleae enter the amount you would like to withdraw?"))
    if cash <= balance:
        balance = balance-cash
        print('you now have {} in your account'.format(balance))
        return True
    else:
        print('you do not have enough money in your account')
        return False


def log(chances):
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

class TestRedOrBlueFunction(TestCase):
    def test_pin_code(self):
        expected = True
        result = pin_code(pin='1234')
        self.assertEqual(expected, result)
    def test_pin_code_incorrect(self):
        expected = False
        result = pin_code(pin='0000')
        self.assertEqual(expected, result)
    def test_withdrawal_incorrect(self):
        expected = False
        #need to put cash at 150
        result = withdrawal(cash=150)
        self.assertEqual(expected, result)

    def test_withdrawal_correct(self):
        expected = True
        #need to put cash at 10
        result = withdrawal(cash=10)
        self.assertEqual(expected, result)

    def test_log_toomanyattempt(self):
        expected = False
        result = log(chances=4)
        self.assertEqual(expected, result)

