# # syntax

# class Student:
#     age = 20

#     def __init__(self, name, level, address):
#         print("This is constructor")
#         self.name = name
#         self.level = level
#         self.address = address

#     def displauStudentDetails(self):
#         print(f"Name: {self.name}")
#         print(f"Level: {self.level}")
#         print(f"Address: {self.address}")
        
        
# first_student = Student("Surya", "Beginner", "Chennai")
# second_student = Student("Rahul", "Intermediate", "Bangalore")
# print(first_student.age)
# print(second_student.age)

# first_student.displauStudentDetails()
# second_student.displauStudentDetails()


class Student:
    school_name = "ABC School"
    
    def __init__(self, ID, name, grade):
        self.ID = ID
        self.name = name
        self.grade = grade

    # #  instance method
    # def display_student_details(self):
    #     print(self.ID)
    #     print(self.name)
    #     print(self.grade)    

    # class method

    def display_student_details():
        print(f"School Name: {Student.school_name}")

student_one = Student(1, "Surya", "A")
Student.display_student_details()