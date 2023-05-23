from DemoCalculator import adder
from DemoDatetime.current import get_current


total = adder.add(1, 5)

print("****************")
print(total)
print("****************")


# example of invoking function from another import
print("=====================")
print(get_current.current_date())
print("=====================")
