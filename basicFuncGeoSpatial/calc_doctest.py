def dec_to_deg_min_sec(deg_dec):
    '''
    >>> dec_to_deg_min_sec(50.084522)
    [50, 5, 4.27919999999915]
    >>> dec_to_deg_min_sec(-5.699057)
    [-5, 41, 56.60519999999934]
    '''

    degrees = int(deg_dec)
    minutes_dec = abs(deg_dec - degrees) * 60
    minutes = int(minutes_dec)
    seconds = (minutes_dec - minutes) * 60
    return [degrees, minutes, seconds]

def deg_min_sec_to_dec(deg,min,sec):
    '''
    >>> deg_min_sec_to_dec(0, 0, 0)
    0.0
    >>> deg_min_sec_to_dec(90, 0, 0)
    90.0
    >>> deg_min_sec_to_dec(90, 60, 0)
    91.0
    >>> deg_min_sec_to_dec(90, 60, 60)
    91.01666666666667
    >>> deg_min_sec_to_dec(50, 5, 4.27919999999915)
    50.084522
    '''
    return deg + min / 60 + sec / 3600

def dec_to_deg_min_sec_unit(deg_dec):
    '''
    >>> dec_to_deg_min_sec_unit(0)
    [0, 0, 0.0]
    >>> dec_to_deg_min_sec_unit(90)
    [90, 0, 0.0]
    >>> dec_to_deg_min_sec_unit(1.5)
    [1, 30, 0.0]
    >>> dec_to_deg_min_sec_unit(50.084522)
    [50, 5, 4.2792]
    '''
    degrees = int(deg_dec)
    minutes = int((deg_dec - degrees) * 60)
    seconds = ((deg_dec - degrees) - minutes / 60) * 3600
    seconds = round(seconds, 4)
    return [degrees, minutes, seconds]

if __name__ == "__main__":

    import doctest
    print(doctest.testmod())
