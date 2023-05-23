
# # Example: function to add two number
# def my_adder(a, b):
#
#     total = a + b
#
#     return total
#
# my_total = my_adder(4, 15)
# print(my_total)

# Example: function to determine if given state has no sales tax

# def has_no_sales_tax(state):
#
#     states_with_no_sales_tax = ['AK', 'DE', 'MT', 'NH', 'OR']
#
#     no_tax = None
#     if state.upper() in states_with_no_sales_tax:
#         no_tax = True
#     else:
#         no_tax = False
#
#     return no_tax

def has_no_sales_tax(state):

    states_with_no_sales_tax = ['AK', 'DE', 'MT', 'NH', 'OR']

    if state.upper() in states_with_no_sales_tax:
        return True
    else:
        return False

user_state = "OR"
tax = has_no_sales_tax(user_state)
print(tax)



