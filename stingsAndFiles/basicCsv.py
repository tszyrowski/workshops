import csv 

student1 = 'Garry Green, gary@myemail.gov, garry1green'
student2 = 'Terry Reed, tr123@school.mail.com, 123tr456'
student3 = ['Jonh', 'Black', 'jb@email.com', 'johny123']
student4 = ['Mark', 'White', 'myschool.co.uk', 'mypass_0']

students = [student1, student2, student3, student4]

for student in students:
    if type(student) == str: 
        students[students.index(student)] = student.replace(",","") .split()
        
for student in students:
    if not '@' in student[2]:
        students[students.index(student)][2] = 'incorrect email'

for student in students:
    print(student)
    
pathToFile = './studentsData.csv'
                                       
with open('./studentsData.csv', 'w', newline='') as myfile:  
    writer = csv.writer(myfile)           
    for student in students:
        writer.writerow(student)
                                
print('finished writing file')

myStudents = []                         # create empty list

with open(pathToFile, 'r') as fileToRead:
    reader = csv.reader(fileToRead)     # create oject to read
    for row in reader:                  # iterate over all rows
        myStudents.append(row)          # add to list
        
print(myStudents)                       # check the output
        
