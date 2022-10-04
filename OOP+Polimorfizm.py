# Один о тот же метод у каждого класса выполняет разные функции

class Employee:
    def __init__(self, name,surname):
        self.name=name
        self.surname=surname
    def work(self):
        return ("I can walk!")
employee=Employee('Alex', "Smith")
print(employee.name)
print(employee.surname)
print(employee.work())

employee2=Employee("Artuom","Kudryshov")
print(employee2.name)
print(employee2.surname)
print(employee2.work())


print("Наследование")
class Developer (Employee):
    def __init__(self,name,surname,language):
        super().__init__(name,surname)
        self.language =language

    def work(self):
        return "I am coding!"


    def get_language(self):
        return  f' My language is {self.__language}'
    def set_language(self,newlang):
        self.__language=newlang
    def get_name(self):
        return  f' My name is {self.__name}'
    def set_name(self,newName):
        self.__name=newName
dev1=Developer("Max","Frolow","Python")
print(dev1.work())
dev1.set_name('Artuom Kudryashov')
print(dev1.get_name())

print("Language of Developers")
print(dev1.language)
dev1.set_language("fdsfdsfdsfdsfdsfsd")
print(dev1.get_language())
# print(dev1.get_language())

class Tester (Employee):
    def __init__(self,name,surname,language, test_frameWork):
        super().__init__(name,surname)
        self.language =language
        self.test_framework=test_frameWork
    def work (self):
        return "I can write test!"
    print('Tester')

tester1=Tester('Anna','Fedorova','Java','TestNG')
print(tester1.language)
print(tester1.language)
print(tester1.work())
print("What belongs to what")
print(issubclass(Tester,Employee))
tester1.language="Python"
print(tester1.language)
# print(tester1.language())




