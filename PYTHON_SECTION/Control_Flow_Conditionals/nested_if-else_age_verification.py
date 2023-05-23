
theater_name = 'XYZ'
rated_r_age_limit = 17

print(f"Welcome to {theater_name} theaters!!!")

user_input = input("Enter your age: ")
print(f"User input is: {user_input}")

if int(user_input) >= rated_r_age_limit:
    print("Enjoy the movie")
else:
    adult_present = input("Is another adult with you? yes or no: ")
    if adult_present.lower() == 'yes':
        print("Enjoy the movie")
    else:
        print("You must be 17 to watch the movie.")