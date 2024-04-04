class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def public_method(self):
        print(f"Hi, my name is {self.name} my age is {self.age}")
    def _protected_method(self):
        print(f"Hi, my name is {self.name} my age is {self.age}")
    def __private_method(self):
        print(f"Hi, my name is {self.name} my age is {self.age}")

if __name__ == "__main__":
    p = Person("Roma", 12)
    p.public_method() # просто выведет имя и возрост
    p._protected_method() # покажет предупреждение
    p.__private_method() # этот метод не существует