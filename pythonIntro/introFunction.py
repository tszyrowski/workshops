'''
@author: T
'''
names = ['Anna', 'Chris', 'Bella', 'Dan', 'Greg']

def greetings(nameList):    # function definition
    myGreetings = []        # decleare a list to store all greetings
    
    for name in names:
        myGreetings.append('Oh Dear %s ' % name)
    else:
        myGreetings.append('Hi Buddy %s ' % name)
        
    return myGreetings      # this is what function produces

whatToSay = greetings(names)# we create a variable to storrre all greetings
print(whatToSay)
    