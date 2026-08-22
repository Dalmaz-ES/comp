from os import name


# CLASS VARIABLES = shared among all instances of a class
#                   defined outside the constructor
#                   allow you to share data among all objects created from that list



class Student:

    class_year = 2025
    num_students = 0


    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("Charles", 15)
student2 = Student("Carlos", 16)
student3 = Student("Alex", 17)
student4 = Student("Max", 18)

#print(student1.name)
#print(student1.age)
#print(Student.class_year)
#print(Student.num_students)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
print(student1.name+ ",", student2.name+ ",", student3.name+ ",", student4.name)


