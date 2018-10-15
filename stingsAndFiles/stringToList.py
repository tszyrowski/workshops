myStudent = 'Tim, tim@email.gov'

print(type(myStudent))
print(isinstance(myStudent, str))
# BUT str IS SPECIAL TYPE NOT SIMPLY list
print(isinstance(myStudent, list))
print(list(myStudent))
''' WE CAN USE SOME OF THE SAME METHODS FOR STRING IN LIST '''
myList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

# BASIC OPERATIONS
print(len(myList), len(myStudent))
print(myList+[19], myStudent+' something')
print(myList*2, myStudent*2)

# BUT SOME OPERATIONS DIFFER
print(myList.remove(16))
print(myStudent.replace('m', ''))

# BUT THEY ARE STILL DIFFERENT:
try:
    print(myList+myStudent)
except Exception as e: print(e)    
#===============================================================================
# 

# SLICING
print(myList[0], myStudent[0])
print(myList[-1], myStudent[-1])
print(myList[9:14], myStudent[9:14])

# CHECK IF VALUE EXISTS
print(myList.count(1), myStudent.count('@'))
print(myList.index(10), myStudent.index('@'))
print(5 in myList, '@' in myStudent)

# BUT STRING CONTAINS MORE THAN A SIMPLE LIST
print(myStudent.split(' '))
try:
    print(myList.split('5'))
except Exception as e: print(e)

#===============================================================================
# moving from list to string
myStudentAsList = myStudent.split()
print(myStudentAsList)

myStrudentFromList = ' '.join(myStudentAsList)
print(myStrudentFromList)

# BUT WATCH OUT WHAT YOU JOIN
print(' '.join(myStudent))


#===============================================================================
# Some Sting methods
print(myStudent.upper())
# upper up first character in each word
print(myStudent.title())
# lower case for all letters
print(myStudent.casefold())
# take second word and upper up first letter
print(myStudent.split(' ')[1].capitalize())

#===============================================================================
# Validate strings
print('*' in 'you are *****!')
print('you are *****!'.count('*'))
print('12345'.isnumeric(), 'abs45'.isnumeric())
print('abcde'.isalpha(), 'abc45'.isalpha())
print('abc45'.isalnum())

# check if any character in string is a digit 
print(any(char.isdigit() for char in 'abc45'))
#===============================================================================
