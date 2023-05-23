"""
Create a class that has basic calculating functions.

You can have as many methods as you like but here are few suggestions.
* method to take two numbers and add them and return the sum
* method to take two numbers and subtract the second number from the first number and return the diff
* method to take two numbers and return the multiplication of the two
* method to divide two numbers and return the result (first number divided by second number)

"""

class BasicCalculator:

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def devide(self, x, y):
        return x/y

mycalc = BasicCalculator()
my_sum = mycalc.add(2,3)
print(my_sum)
print(mycalc.subtract(10, 4))

class BasicCalculatorV2:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def subtract(self):
        return self.x - self.y

    def multiply(self):
        return self.x * self.y

    def devide(self):
        return self.x/self.y

mycalc2 = BasicCalculatorV2(15, 11)
my_sum = mycalc2.add()
print(my_sum)
