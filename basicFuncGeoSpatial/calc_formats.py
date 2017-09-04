def deg_min_str_to_dec(position):
    '''
    >>> pos = '50 05.0713061 N'
    >>> deg_min_str_to_dec(pos)
    50.08452177
    >>> deg_min_str_to_dec('005 41.9434092 W')
    -5.69905682
    >>> deg_min_str_to_dec('50 05.0713061 N')
    50.08452177
    >>> deg_min_str_to_dec('55;18.7116860N')
    55.31186143
    >>> deg_min_str_to_dec('5023.1994,N')
    50.38665667
    >>> deg_min_str_to_dec('00408.6421,W')
    -4.144035
    >>> deg_min_str_to_dec('5023.1994,S')
    -50.38665667
    >>> deg_min_str_to_dec('00408.6421,E')
    4.144035
    '''
    if " " in position:
        l = position.split(" ")
        deg = int(l[0])
        minut = float(l[1])
        
