

# from src.util.dbHelper import DBHelper  # example,  we would import it
import random

class DatabaseHelper:

    def __init__(self, database_address, username, password):
        self.connection = 'I just connected'

    def write_to_db(self):
        print("writing.....")

    def read_from_db(self):
        print('read...')

class AuthHelper:
    pass
# Example of inheritance
class Account(DatabaseHelper):

    def __init__(self, user_id, database_address, username, password, currency='USD',):
        super().__init__(database_address, username, password)
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
        self.write_to_db()
        return random.randint(100, 1000)

    def __write_balance_to_db(self):
        self.read_from_db()
        print("Saving to db.")

# Example of composition
class Account(object):

    def __init__(self, user_id, database_address, username, password, currency='USD',):
        self.user_id = user_id
        self.currency = currency
        self.current_balance = self.__read_balance_from_database()
        print(f"Current balance is: {self.current_balance}")
        self.db_helper = DatabaseHelper(database_address, username, password)
        self.auth = AuthHelper()

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
        self.db_helper.read_from_db()
        return random.randint(100, 1000)

    def __write_balance_to_db(self):
        print("Saving to db.")

        self.db_helper.write_to_db()

my_acct = Account(...)