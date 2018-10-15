'''
@author: http://swcarpentry.github.io/training-course/2015/03/matt-probert-mcq/
'''
x=1; y=2; z=3

def FMA(x,y):
    z=multiply(x,y)
    x=x+z
    return x

def multiply(x,y):
    x=x*y
    return x

z=FMA(1,1)
print(x,y,z)

'''
What will be printed?

1.     1 2 2
2.     2 1 2
3.     4 2 2
'''