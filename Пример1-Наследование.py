class Human:
    def __init__(self, name, age):
        self.name = name  # устанавливаем имя
        self.age = age
    def info(self):
        return f"Hello my name is {self.name}, my age is {self.age}."
class Women(Human):
    def info_women(self):
        return f"Hi, my name is {self.name} my age is {self.age}"
class Men(Human):
    def info_men(self):
        return f"My name is {self.name} my age is {self.age}"
Olga=Women("Olga",45)
Bob1=Men("Bob",62)

print(Olga.info())
print(Bob1.info())