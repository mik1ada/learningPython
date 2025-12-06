import random

class Student:
  def __init__(self, name, surname, age, city):
    self.name = name
    self.surname = surname
    self.age = age
    self.city = city
    self.schoolName = None
    self.fieldOfStudy = None

  def printInfo(self):
    print(self.name, self.surname, self.age, self.city, self.schoolName, self.fieldOfStudy)

class School:
  def __init__(self, name, city):
    self.name = name
    self.city = city
    self.studentsList = []
    self.fieldsOfStudy = ['IT', 'Math', 'Robotics']

  def addStudent(self, student):
    if isinstance(student, Student):
      self.studentsList.append(student)
      student.schoolName = self.name
      student.fieldOfStudy = random.choice(self.fieldsOfStudy)
  
  def printSchoolInfo(self):
    print("School name:", self.name, " City:", self.city, "\nStudents:")
    for student in self.studentsList:
      student.printInfo()

student1 = Student('Michal', 'Brzoza', 30, 'Krakow')
student1.schoolName = 'Tech School'
student1.country = 'USA'
student1.printInfo()
print(student1.country)

student2 = Student('Adam', 'Marek', 21, 'Warsaw')

school = School('Tech School', 'Warsaw')
school.addStudent(student1)
school.addStudent(student2)
school.printSchoolInfo()