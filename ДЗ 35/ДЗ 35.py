import person
import student
import group

man = person.Person('Yurii', 'Ostapenko', 36, 'male')
woman = person.Person('Olga', 'Ivanova' , 34, 'female')
print(man.get_info())

s1 = student.Student('Yurii', 'Ostapenko', 36, 'male', 35643)
s2 = student.Student('Olga', 'Ivanova' , 34, 'female', 64716)
print(s1.get_info())

g = group.Group()
g.add_student(s1)
g.add_student(s2)
g.del_student('Ivanova')
print(g)