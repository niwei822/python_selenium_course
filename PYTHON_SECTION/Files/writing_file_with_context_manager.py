

my_string = "I love to program in Python language"


# # ex 1
with open('./sample_output_2.txt', 'w') as my_f:
    my_f.write(my_string)

# # ex 2
# my_l = ['user1', 'user2', 'user3']
# with open('./sample_output_2.txt', 'w') as my_f:
#     for i in my_l:
#         my_f.write(i)
#         my_f.write('\t')

# # ex 3 (appending)
# var2 = "Also love testing"
# with open('./sample_output_2.txt', 'a') as f:
#     f.write('\n')
#     f.write(var2)
#
# # ex 4
# my_langs = ['Python', 'Js', 'PHP', 'Java', 'Ruby']
# with open('./my_fav_languages.csv', 'w') as f:
#     f.writelines(my_langs)

# ex 5
# my_langs = ['Python', 'Js', 'PHP', 'Java', 'Ruby']
# with open('./my_fav_languages.csv', 'w') as f:
#     str_my_langs = '\n'.join(my_langs)
#     f.write(str_my_langs)