
# # simple try-catch
# try:
#     a = 5 / 0
# except:
#     print("dont divide by 0")

# # Example: catch specific exception
# try:
#     a = 5 / 0
# except ZeroDivisionError:
#     print("dont divide by 0")


# # Example: print the actual error
# try:
#     a = 5 / 0
# except ZeroDivisionError as e:
#     print(f"Error has happened: {e}")

# # Example: print the actual error
# try:
#     # a = 5 / 0
#     print(foo)
# except Exception as e:
#     print(f"Error has happened: {e}")

# # Example: catch multiple exceptions in 1 block
# try:
#     a = 5 / 0
#     b = {'name': 'foo', 'age': 26}
#     x = b['school']
# except (KeyError, ZeroDivisionError):
#     print(f"Error has happened")

# # Example: catch multiple exceptions in multiple blocks
# try:
#     # a = 5 / 0
#     b = {'name': 'foo', 'age': 26}
#     x = b['school']
# except KeyError:
#     print(f"key issue")
# except ZeroDivisionError:
#     print("dividing by zero")


# # Example: raise an exception
# try:
#     a = 5 / 0
#     print(foo)
# except Exception as e:
#     print(f"Error has happened: {e}")
#     raise Exception("Something went wrong")

# Example: re-raise
try:
    a = 5 / 0
    print(foo)
except Exception as e:
    print("Sending notification")
    raise