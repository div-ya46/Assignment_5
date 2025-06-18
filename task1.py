student_marks = {'Mike':87,'Nick':93,'Alice':85}
name= input("Enter the student's name: ")

marks = student_marks.get(name)
if marks != None:
    print("{}'s marks: {}".format(name,marks))
else:
    print('Student not found.')





