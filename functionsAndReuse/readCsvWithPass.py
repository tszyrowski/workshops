import csv 

csvFile = '../stingsAndFiles/studentsData.csv'

def readData(csvFile):
    
    students = []                         
    with open(csvFile, 'r') as fileToRead:
        reader = csv.reader(fileToRead)     
        for row in reader:                 
            students.append(row)         
    return students 

for student in readData(csvFile):
    print(student)