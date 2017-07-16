'''
Created on 17 Jul 2017

@author: T
'''

def fileWriter():
    file = open("testfile.txt","w") 
     
    file.write("Hello World") 
    file.write("This is our new text file") 
    file.write("and this is another line.") 
    file.write("Why? Because we can.") 
     
    file.close() 
    
def fileReader():
    file = open("testfile.txt", "r") 
    print(file.read()) 
    
fileReader()