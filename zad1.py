class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        return self.marks > 50

    def __str__(self):
        return f'Student: {self.name}, {self.marks}'

if __name__=="__main__":

    student1 = Student('Tomasz', 65)
    student2 = Student('Aleksandra', 50)
    print(student1.is_passed())
    print(student2.is_passed())
