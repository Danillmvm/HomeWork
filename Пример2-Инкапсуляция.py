class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def classic_speak(self):
        print(f"Hi, my name is {self.name} my age is {self.age}")
    def _vip_speak(self):
        print(f"Hi, my name is {self.name} my age is {self.age}")
    def __super_vip_speak(self):
        print(f"Hi, my name is {self.name} my age is {self.age}")

if __name__ == "__main__":
    p = User("Micha", 34)
    p.classic_speak() # просто выведет имя и возрост
    p._vip_speak() # покажет предупреждение
    p.__super_vip_speak() # этот метод не существует