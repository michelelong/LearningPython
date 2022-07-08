#!/usr/local/bin/python3

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Multiple inheritance is possible in Python (Parent1, Parent2), but not a good idea
# Order of inheritance is important if methods are overridden
class Student(Person):
    def __init__(self, name, age):
        # Inherit name and age from Person
        super().__init__(name, age)
        # Student specific attributes not a part of Person
        self.classes = []
        self.grades = []

    def addClass(self, classID):
        self.classes.append(classID)

    def getClasses(self):
        return self.classes

    def addGrade(self, g):
        self.grades.append(g)

    def getGradeAvg(self):
        average = sum(self.grades) / len(self.grades)
        return average

    def greet(self, other):
        print("Hello, %s. My name is %s." % (other.name, self.name))


m = Student("Michele", 45)
m.addClass("COMP091")
m.addClass("COMP0122")
print(m.getClasses())
m.addGrade(92)
m.addGrade(88)
print("Average grade: ", m.getGradeAvg())

print()

class Graduate(Student):
    def __init__(self, name, age):
        super().__init__(name, age)

    def greet(self, other):
        # Optional call to Student greet method
        super().greet(other)

        # Add greeting specific to Graduate
        print("You are still a lowly student, %s? I am a college graduate!" % (other.name))


grad = Graduate("Emily", 21)
grad.greet(m)
