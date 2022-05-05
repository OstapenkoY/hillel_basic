from person import *

class Student(Person):

    def __init__(self, fname, lname, age, sex, student_ID):
        super().__init__(fname, lname, age, sex)
        self.student_ID = student_ID

    def get_info(self):
        return f"Full name: {self.fname} {self.lname}, Age: {self.age}, Sex: {self.sex}, ID: {self.student_ID}"