'''
@author: T
'''
names = ['Anna', 'Chris', 'Bella', 'Dan', 'Greg']
names2 = ['Tom', "Dora", 'Fox', "Michael"]

def greetings(nameList):    # function definition
    myGreetings = []        # decleare a list to store all greetings
    

    for name in nameList:
        if name[-1] == 'a':
            myGreetings.append('Oh Dear %s ' % name)
        else:
            myGreetings.append('Hi Buddy %s ' % name)
        
    return myGreetings      # this is what function produces

whatToSay = greetings(names)# we create a variable to storrre all greetings
whatElse = greetings(names2)
print(whatToSay)
print(whatElse)
    