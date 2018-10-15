'''
Each password should:
- contain more then 8 characters
- but less then 15 characters
- at least one capital letter
- at least one digit
- can't contain characters such as: '@', '+', '-'
'''

# build a script checking:

pwd1 = 'I_am_the_8351'
pwd2 = 'feelgood@home'

notPermited = ['@', '+', '-']

pdw1Validator = True
if any(ch in pwd1 for ch in notPermited):
    pwd1Validator = False
if not any(char.isdigit() for char in pwd1):
    pwd1Validator = False
if not 7 < len(pwd1) < 16:
    pwd1Validator = False
if not any(char.isupper() for char in pwd1):
    pwd1Validator = False

pdw2Validator = False
if any(char in pwd2 for char in notPermited):
    pwd2Validator = False
if not any(char.isdigit() for char in pwd2):
    pwd2Validator = False
if not 7 < len(pwd2) < 16:
    pwd2Validator = False
if not any(char.isupper() for char in pwd2):
    pwd2Validator = False

# print the output:
print('string "{}" is {} password'.format(pwd1, pdw1Validator))
print('string "{}" is {} password'.format(pwd2, pdw2Validator))