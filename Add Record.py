class Student:
    #master function of class
    def __init__(self, name, father_name, age, class_):
        self.name = name
        self.father_name = father_name
        self.age = age
        self.class_ = class_

students = [] #creating array/list for students
total_students = 0 #number for students that have been registered
#creating dictionary for seats of each class, assuming key as class and value as seats
seats = {
    1: 20,
    2: 20,
    3: 20,
    4: 20,
    5: 20,
    6: 20,
    7: 20,
    8: 20,
    9: 20,
    10: 20,
    11: 20,
    12: 20
}

def add_student(): #function for adding student
    name1 = input("Enter the student's name: ") #asking for student's name
    father_name1 = input("Enter the student's father's name: ") #asking for student's father name
    age1 = int(input("Enter the student's age: ")) #asking for student's age
    #creating dictionary for class tags, assuming key as given menu option to user and value as class tag
    class_names = {1: 'Grade 1', 2: 'Grade 2', 3: 'Grade 3', 4: 'Grade 4', 5: 'Grade 5', 6: 'Grade 6', 7: 'Grade 7', 8: 'Grade 8', 9: 'Grade 9', 10: 'Grade 10', 11: 'Grade 11', 12: 'Grade 12'}

#creating if and else only student between age 6 to 22 will be registered and for other ages(else) print invalid ages
    if age1 < 23 and age1 > 0:
        #giving list of classes to user according to age 
        if age1 >= 6 and age1 <= 9:
            print("Classes for age 6-9:")
            for class_ in range(1, 5):#calling classes tags dictionary by using key
                print(f"{class_}. {class_names[class_]} (seats available: {seats[class_]})")#using interpolation method to show list of available classes by using only one line
        elif age1 < 14 and age1 >= 10:
            print("Classes for age between 10-13.")
            for class_ in range(5, 9):
                print(f"{class_}. {class_names[class_]} (seats available: {seats[class_]})")
        elif age1 < 18 and age1 > 10:
            for class_ in range(9, 11):
                print(f"{class_}. {class_names[class_]} (seats available: {seats[class_]})")
        elif age1 <= 22 and age1 >= 18:
            print("Classes for age 18 and above:")
            for class_ in range(11, 13):
                print(f"{class_}. {class_names[class_]} (seats available: {seats[class_]})")
        #after giving appropriate options getting the user that in which he wanted to add the student
        class_ = int(input("Enter the class number: "))
        class_name = class_names.get(class_)#calling class dictionary to get Grade name in seperate variable
        #validating input from user
        if age1 >= 6 and age1 <= 9 and 1 <= class_ <= 4:
            seats[class_] -= 1
        elif age1 < 14 and age1 >= 10 and 5 <= class_ <= 8:
            seats[class_] -= 1
        elif age1 < 18 and age1 > 10:
            if class_ == 9 or class_ == 10:
                seats[class_] -= 1
            else:
                print("Invalid Class number")
                input("Press enter to continue....")
                return
        elif age1 <= 22 and age1 >= 18 and class_ == 11 or class_ == 12:
            seats[class_] -= 1
        else:
            print("Invalid Class number")
            input("Enter to continue...")
            return
    else:
        print("There is no classes available for entered age.")
        input("Press Enter to continue....")
        return
#after getting all required parameters, now we finally call our function or object created in student class
    new_student = Student(name1, father_name1, age1, class_)
    students.append(new_student)#adding student's data to student list/array
    global total_students#creating global variable for total number of students
    total_students += 1#incrementing total students
    print(f"Student {name1} has been added to Class: {class_}!, with the GR number: {total_students}")#printing the gr no, and confirmation of student admission
    input("Press Enter to continue....")
    print("")

def view_student():#creating the second menu option to show the student's data
    gr_no = int(input("Enter the GR number of the student: "))#getting gr no to access that specific student data
    if gr_no < 1 or gr_no > total_students:#checking gr number is correct or incorrect
        print("Invalid GR number.")
        return
    student = students[gr_no - 1]
    #printing student's data
    print(f"Student name: {student.name}")
    print(f"Student father's name: {student.father_name}")
    print(f"Student age: {student.age}")
    print(f"Student class: {student.class_}")
    input("Press Enter to continue....")
    print("")

while True:#creating counter for student that have been added
    if total_students == 0:
        print("No students registered yet.")
    else:
        print(f"We currently have {total_students} registered students in our application")
    #printing menu options
    print("")
    print("Enter an option: ")
    print("1. Add a student")
    print("2. View a student's data")
    print("3. Exit the program")
    print("")

    #getting menu option
    option = int(input())

    if option == 1:
        add_student()
    elif option == 2:
        view_student()
    elif option == 3:
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")
        print("")
