
# Example 1
# a = 20
# b = 5
# c = 30
# d = 10
#
#
# if a < b:
#     print("'a' is less than 'b'.")
# elif (a > b) and (a < c):
#     print("'a' is greater than 'b'.")
# else:
#     print("N/A")

# Example 2
shows = ["Friends", "The Office", "Breaking Bad", "Stranger Things"]
movies = ["Rocky", "Jaws", "Batman", "Wonder Woman"]

my_choice = 'jaws'

# if my_choice in shows:
#     print("Your choice is a show.")
# elif my_choice in movies:
#     print("Your choice is a movie")
# else:
#     print("Your choice is unknown.")


# Example 3
if (my_choice in shows) or (my_choice in movies):
    print("your choice is valid")
else:
    print("Unknown")