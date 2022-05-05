class Person:

    def __init__(self, fname, lname, age, sex):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.sex = sex

    def get_info(self):
        return f"Full name: {self.fname} {self.lname}, Age: {self.age}, Sex: {self.sex}"

class Student(Person):

    def __init__(self, fname, lname, age, sex, student_ID):
        super().__init__(fname, lname, age, sex)
        self.student_ID = student_ID

    def get_info(self):
        return f"Full name: {self.fname} {self.lname}, Age: {self.age}, Sex: {self.sex}, ID: {self.student_ID}"

class Group:

    def __init__(self):
        self.student_list = []

    def add_student(self, student):
        if student in self.student_list:
            print('The student is already in the group.')
        else:
            self.student_list.append(student)
            print(f"Student {student.fname + ' ' + student.lname} added to group")

    def del_student(self, student_name):
        student = self.find_student(student_name)
        if student:
            del self.student_list[self.student_list.index(student)]
            print(f"Student {student.fname + ' ' + student.lname} removed from the group")
        else:
            print('No such student')

    def find_student(self, lname):
        self.lname_list = [i.lname for i in self.student_list]
        if lname in self.lname_list:
            return self.student_list[self.lname_list.index(lname)]
        else:
            return None

    def __str__(self):
        return f"{', '.join([i.fname + ' ' + i.lname for i in self.student_list])}"

student1 = Student('Ivan', 'Goncharov', 31, 'male', '11111')
student2 = Student('Oleg', 'Pushkin', 32, 'male', '22222')
student3 = Student('Viktoria', 'Shumilova', 31, 'female', '33333')
student4 = Student('Nazar', 'Ivanov', 33, 'male', '44444')

group = Group()
group.add_student(student1)
group.add_student(student2)
group.add_student(student3)
group.add_student(student4)
print(group)
print('_' * 50)
group.del_student("Pushkin")
print(group)
print('_' * 50)
group.del_student(student4)
print('_' * 50)

