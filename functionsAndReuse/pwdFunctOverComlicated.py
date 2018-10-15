def pwdValidator(pwd, notPermited = ['@', '+', '-']):
    return (checkChars(pwd, notPermited) and checkDigits(pwd) and checkLength(pwd) and checkUpper(pwd))

def checkChars(pwd, notPermited):
    if any(ch in pwd for ch in notPermited):
        return False
    else: return True
    
def checkDigits(pwd):
    if not any(char.isdigit() for char in pwd):
        return False
    else: return True
def checkLength(pwd):
    if not 7 < len(pwd) < 16:
        return False
    else: return True
    
def checkUpper(pwd):
    if not any(char.isupper() for char in pwd):
        return False
    else: return True

print('"{}" is {} password'.format('I_am_the_8351',pwdValidator('I_am_the_8351')))
