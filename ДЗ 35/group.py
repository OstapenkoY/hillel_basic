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