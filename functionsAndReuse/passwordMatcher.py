
def pwdMatcher(firstName, LastName, pwd, students):
    ''' 
    function expect first, lastname and pwd check match in data
    >>> students = [['Garry', 'Green', 'garry1green'],['Tim', 'Lee', '123tr456'], ['Jo', 'Black','johny123']]
    >>> pwdMatcher('Garry', 'Green', 'garry1green', students)
    True
    >>> pwdMatcher('Garry', 'Green', 'johny123', students)
    False
    >>> pwdMatcher('Garry', 'garry1green', 'Green', students)
    True
    '''
    doesMatch=False
    
    # find entry with password
    for student in students:
        try:
            entry = student.index(pwd)
        except ValueError:
            continue
        # only if there is a list with password and it contains names
        if entry and student.count(firstName) and student.count(LastName):
            doesMatch = True        # change value to true
            
    return doesMatch

if __name__ == '__main__':
    import doctest                  
    doctest.testmod(verbose=True)   