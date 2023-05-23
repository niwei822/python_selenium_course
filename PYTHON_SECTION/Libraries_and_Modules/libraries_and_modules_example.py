######################################
# random
# https://docs.python.org/3/library/random.html
# * look ap the docmenation
# * I use it 3 things: generate a random number, get a random item from a list, randomize a list

import random
my_num = random.randint(100, 200)
my_num = random.randrange(30)

my_list = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']

# randomize a list
random.shuffle(my_list)

# get a random item
my_rand_choice = random.choice(my_list)

# get a random list
my_rand_sample = random.sample(my_list, 2)

