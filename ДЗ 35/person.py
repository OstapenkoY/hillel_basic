class Person:

    def __init__(self, fname, lname, age, sex):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.sex = sex

    def get_info(self):
        return f"Full name: {self.fname} {self.lname}, Age: {self.age}, Sex: {self.sex}"