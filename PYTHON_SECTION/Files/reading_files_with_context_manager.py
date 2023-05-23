

# # example 1
sample_file = './sample_files/programming_language_wikipedia.txt'

with open(sample_file, 'r') as f:
    content = f.read()
print(content)

# example 2
# countries_file = './sample_files/list_of_countries_with_no_comma.txt'
# with open(countries_file, 'r') as my_f:
#     countries = my_f.read()
# list_of_c = countries.split('\n')

# example 3
# countries_file = './sample_files/list_of_countries_with_no_comma.txt'
# with open(countries_file, 'r') as my_f:
#     countries = my_f.readlines()

# list_of_c = countries.split('\n')
# list_of_c = [i.strip() for i in countries]
# print(list_of_c)