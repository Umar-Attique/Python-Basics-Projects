# a-z
# 0-9
# . _
# one time @
# two or three word after.

import re
email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}"
choice ='y'
while choice == 'y':
    choice = input("Press {y} to continue and {n} to exit : ")
    if choice == 'y':
            user_email = input("Enter your email : ")
            if re.search(email_condition,user_email):
                print("Right email")
            else:
                print("Wrong email")
    elif choice == 'n':
        print("Thank you")
        break
