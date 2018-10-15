student1 = 'Garry Green, gary@myemail.gov, garry1green'
student2 = 'Terry Reed, tr123@school.mail.com, 123tr456'

fileHandle = open('./studentData.txt', "a")
fileHandle.write(student1)
fileHandle.write(student2+'\n')
fileHandle.close()

print('the file was created and you can see it now on the system')
print('Now I will read it back and print out')

newFileHandle = open('./studentData.txt', "r")
fileContent = newFileHandle.read()

print(fileContent)