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

V1:
- Create 20 emails for each domain
- Output a csv file with one email on each line and each line ending with a comma
- Output file name: out_generate_random_email_with_list_of_domains_v1.csv
"""
import random
import string

list_of_domains = ['supersqa.com', 'gmail.com', 'yahoo.com', 'outlook.com', 'msn.com']

length_of_email = 10  # each email has 10 characters
letters = string.ascii_lowercase
output_path = 'out_generate_random_email_with_list_of_domains_v1.csv'

# generate the random emails and store in a list
all_emails = []
for domain in list_of_domains:
    for i in range(20):
        random_string = ''.join(random.choice(letters) for i in range(length_of_email))
        # email = random_string + '@' + domain
        # email = "{}@{}".format(random_string, domain)
        email = f"{random_string}@{domain}"
        all_emails.append(email)

# take the list and write file
with open(output_path, 'w') as f:
    # option 1
    # for email in all_emails:
    #     f.write(email)
    #     f.write(',\n')

    # option 2
    # all_emails_str = ',\n'.join(all_emails)
    # f.write(all_emails_str)

    # option 2.1
    f.write(',\n'.join(all_emails))












