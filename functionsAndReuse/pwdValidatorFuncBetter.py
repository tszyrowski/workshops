


def pwdValidator(pwd, notPermited = ['@', '+', '-']):
    ''' check if password is good 
    >>> pwdValidator('I_am_the_8351')
    True
    >>> pwdValidator('feelgood@home')
    False
    ''' 

    if any(ch in pwd for ch in notPermited):
        return False
    if not any(char.isdigit() for char in pwd):
        return False
    if not 7 < len(pwd) < 16:
        return False
    if not any(char.isupper() for char in pwd):
        return False
    return True

if __name__ == '__main__':
    import doctest                  # doctest checks documentation
    doctest.testmod(verbose=True)   # and compare results with expected
