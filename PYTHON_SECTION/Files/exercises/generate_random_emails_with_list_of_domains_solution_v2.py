"""
Exercises:
Create a file with list of randomly generated email addresses.
The email addresses must have domain name from the
given list of domains.
* Domain list is provided as variable 'list_of_domains'

HINT:
To generate random string with all lower case you can use this code
import random
import string
letters = string.ascii_lowercase
random_string = ''.join(random.choice(letters) for i in range(length))

V2:
- Create 100 total emails with domains randomly elected from the list. So the number of emails
for each domain will be unknown.
- Output a csv file with one email on each line and each line ending with a comma
- Output file name: out_generate_random_email_with_list_of_domains_v2.csv

** the difference from V1 is the domains are random for this one.
"""

import random
import string


list_of_domains = ['supersqa.com', 'gmail.com', 'yahoo.com', 'outlook.com', 'msn.com']

length_of_email = 10  # each email is 10 characters long
total_number_of_emails = 100
output_file = 'out_generate_random_email_with_list_of_domains_v2.csv'
letters = string.ascii_lowercase

# OPTION 1 SOLUTION
# all_emails = []
# for i in range(100):
#     # option 1
#     rand_domain = random.choice(list_of_domains)
#     random_string = ''.join(random.choice(letters) for i in range(length_of_email))
#     # rand_email = random_string + '@' + rand_domain
#     rand_email = f"{random_string}@{rand_domain}"
#     all_emails.append(rand_email)
#
#     # option 2
#     # all_emails.append(f"{''.join(random.choice(letters) for i in range(length_of_email))}@{random.choice(list_of_domains)}")
#
#
# with open(output_file, 'w') as f:
#     f.write(',\n'.join(all_emails))


# OPTION 2 SOLUTION
with open(output_file, 'w') as f:
    for i in range(100):
        # option 1
        rand_domain = random.choice(list_of_domains)
        random_string = ''.join(random.choice(letters) for i in range(length_of_email))
        # rand_email = random_string + '@' + rand_domain
        rand_email = f"{random_string}@{rand_domain}"
        f.write(rand_email + ',\n')












