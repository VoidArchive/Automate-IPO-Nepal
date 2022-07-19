from colorama import Fore
from meroshare import MeroShare
import json


asci_art = '''
                  .----.
      .---------. | == |
      |.-"""""-. | |----|
      | | | | | == |
      | | | | |----|
      |'-.....-' | |: : : : |
      `"")---(""` | ___.|
     /:::::::::::\" _  "
    /:::=======:::\`\`\
'''
users = json.load(open('data/data.json', encoding='utf-8-sig'))

print(Fore.MAGENTA + asci_art)
print(Fore.MAGENTA + 'Welcome to IPO Automation for Meroshare')


while users:
    user_input = input('Enter: Apply(a) or Check (c): ')
    if user_input.lower() == 'c':
        meroshare = MeroShare()

        for user in users:
            try:
                meroshare.login(
                    name=user['Name'],
                    depository=user['DP'],
                    username=user['Username'],
                    password=user['Password']
                )

                print(meroshare.get_result(0))
                meroshare.logout()
            except:
                print(f"Couldn't Log In on: {user['Name']}")

        break

    elif user_input.lower() == 'a':
        meroshare = MeroShare()
        break
    else:
        print("Please Enter a or c for apply and check")
