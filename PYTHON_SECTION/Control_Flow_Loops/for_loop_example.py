
# Example 1
# my_list = ['house', 'car', 'bike', 'boat']
#
# for i in my_list:
#     print(i)
#     print('----------')
#
# fruits = ['Orange', 'Apple', 'Banana']
# for j in fruits:
#     print(j)

#Example 2
# # print out words that are 3 or less characters
# quote = "Give a man a program, frustrate him for a day. Teach a man to program, frustrate him for a lifetime."
# words_list = quote.split()
# print(words_list)
# for i in words_list:
#     if len(i) <= 3:
#         print(i)
#     else:
#         pass

# print out words that are 3 or less characters
# quote = "Give a man a program, frustrate him for a day. Teach a man to program, frustrate him for a lifetime."
# for i in quote.split():
#     if len(i) <= 3:
#         print(i)
#     else:
#         pass

# Example 3
# collect the small words (3 or less characters) into a list and print the list
quote = "Give a man a program, frustrate him for a day. Teach a man to program, frustrate him for a lifetime."
small_words = []
for i in quote.split():
    if len(i) <= 3:
        small_words.append(i)
print(small_words)

# Assignment: what happens if you try to loop an empty list?