import re

email_condition = "^[a-z]+[ \._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

email = input("enter your email here:-")

if(re.search(email_condition, email)):
    print("right email")
else:
    print("wrong email")