
notPermited = ['@', '+', '-']

def pwdValidator(pwd):
    ''' takes string and returns:
    true if valid password
    false if invalid password 
    ''' 
    
    pwdValid = True
    if any(ch in pwd for ch in notPermited):
        pwdValid = False
    if not any(char.isdigit() for char in pwd):
        pwdValid = False
    if not 7 < len(pwd) < 16:
        pwdValid = False
    if not any(char.isupper() for char in pwd):
        pwdValid = False
    return pwdValid

if __name__ == '__main__':
    
    pwd1 = 'I_am_the_8351'
    pwd1Valid = pwdValidator(pwd1)
    print('string "{}" is {} password'.format(pwd1, pwd1Valid))
    
    print('string "{}" is {} password'.format('feelgood@home', pwdValidator('feelgood@home')))