

sample_file = './sample_files/programming_language_wikipedia.txt'

# demo 1
my_file = open(sample_file, 'r')
content = my_file.read()
my_file.close()
my_content_list = content.split('\n\n')

# demo 2
# my_file = open(sample_file, 'r')
# content = my_file.readlines()
# my_file.close()
# print(content)

# demo 3
# my_file = open(sample_file, 'r')
# content = my_file.readline()
# my_file.close()


# gotcha!!!
# the .seek() method
# my_file = open(sample_file, 'r')
# content = my_file.read()
# print(content)
# # my_file.seek(0)
# print("-----")
# content2 = my_file.read()
#
# print(content2)
# print('********')
# my_file.close()