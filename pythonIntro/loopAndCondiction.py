'''
@author: T
'''
names = ['Anna', 'Chris', 'Bella', 'Dan', 'Greg']
for name in names:
    print('hello %s' % name)

print('=====================\nAdding some condition \n=====================')

for name in names:
    if name[-1] == "a":
        print('Oh dear %s ' % name)
    else:
        print('Hi Buddy %s ' % name)
    
