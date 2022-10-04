class Employee:
    def __init__(self, name,surname):
        self.name=name
        self.surname=surname
    def walk(self):
        return ("I can walk!")
employee=Employee('Alex', "Smith")
print(employee.name)
print(employee.surname)
print(employee.walk())

employee2=Employee("Artuom","Kudryshov")
print(employee2.name)
print(employee2.surname)
print(employee2.walk())


print("Наследование")
class Developer (Employee):
    def __init__(self,name,surname,language):
        super().__init__(name,surname)
        self.language =language

    def coding(self):
        return "I am coding!"
dev1=Developer("Max","Frolow","Python")
print(dev1.walk())
print(dev1.name)
print(dev1.language)


class Tester (Employee):
    def __init__(self,name,surname,language, test_frameWork):
        super().__init__(name,surname)
        self.language =language
        self.test_framework=test_frameWork
    def Testing (self):
        return "I can write test!"

tester1=Tester('Anna','Fedorova','Java','TestNG')
print(tester1.language)
print(tester1.Testing())
print("What belongs to what")
print(issubclass(Tester,Employee))
