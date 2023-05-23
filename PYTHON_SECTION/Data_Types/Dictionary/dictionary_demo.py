source env/bin/activatepip3 freeze > requirements.txt

capitals = {"USA": "Washington DC", "France": "Paris", "Turkey": "Ankara"}

# print(type(capitals))

# # getting items from the dictionary
# france_capital = capitals["France"]
# print(france_capital)
#
# france_capital2 = capitals.get("France")
# print(france_capital2)

# get key that does not exist
# ethiopia_capital = capitals["Ethiopia"]  # will fail
# print(ethiopia_capital)

# print("===========")
# ethiopia_capital = capitals.get("Ethiopia")
# print(ethiopia_capital)
#
# # return a default value if key does not exist
# ethiopia_capital2 = capitals.get("Ethiopia","NOT EXIST")
# print(ethiopia_capital2)

# ################
# # Adding item to dictionary
# # Option 1
# capitals = {"USA": "Washington DC", "France": "Paris", "Turkey": "Ankara"}
# print("Before add")
# print(capitals)
# capitals["Kenya"] = "Nairobi"
# print("After add")
# print(capitals)
#
# # Option 2
# capitals.update({"India": "New Delhi"})
# print("Add option2")
# print(capitals)
#
# # Assignment: what if you try to add a key that already exist?
# # Assignment: lookup/study what does the method 'setdefault' do?

# ################
# capitals = {"USA": "Washington DC", "France": "Paris", "Turkey": "Ankara"}
# all_keys = capitals.keys()
# all_values = capitals.values()
# print(all_keys[0])
# print(all_values)
# # Try Python 3 and Python 2 using terminal/CMD.

# Another example of a dictionary
employee = {"name": "John Doe",
            "age": 25,
            "phone": 15101111111,
            "title": "Sr. Software Engineer",
            "skills": ["AWS", "Python", "Java", "Docker"]
            }

e_name = employee['name']
e_age = employee['age']
e_skills = employee['skills']
print(type(e_skills))
user_skill_count = len(e_skills)
print(f"User has {user_skill_count} skills.")
print("User has {} skills".format(user_skill_count))






