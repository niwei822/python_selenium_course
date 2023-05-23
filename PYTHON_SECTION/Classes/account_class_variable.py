

import random

class Account(object):

    minimum_investment_amount = 50

    def __init__(self, user_id, currency='USD'):
        self.user_id = user_id
        self.currency = currency
        self.current_balance = self.__read_balance_from_database()
        print(f"Current balance is: {self.current_balance}")

    def withdraw(self, amount):
        self.current_balance = self.current_balance - float(amount)
        print(f"New balance after withdraw: {self.current_balance}")

    def deposit(self, amount):
        self.current_balance = self.current_balance + float(amount)
        print(f"New balance after deposit: {self.current_balance}")

    def generate_statement(self, start_date, end_date):
        pass

    def __read_balance_from_database(self):
        print(f"Getting balance from db for: {self.user_id}")
        return random.randint(100, 1000)

    def create_new_investment_account(self, balance):

        if Account.minimum_investment_amount > float(balance):
            raise Exception("Can not open investment account without the min amount.")
        else:
            print("Account created")


acct1 = Account(123)
acct2 = Account(987)
print('=========')
print(f"acct1 min: {acct1.minimum_investment_amount}")
print(f"acct2 min: {acct2.minimum_investment_amount}")

acct1.minimum_investment_amount = 100

print(f"acct1 min: {acct1.minimum_investment_amount}")
print(f"acct2 min: {acct2.minimum_investment_amount}")

acct3 = Account(333)
print(f"acct3 min: {acct3.minimum_investment_amount}")