class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def speak(self):
        return f"Hello. I'm {self.name}"    
    
class Vip_user(User):
    def speak(self):
        return f"hi I'm a vip user my name is {self.name}"
    
class Classic_user(User):
    def speak(self):
        return f"hi I'm a classic user my name is {self.name}"
    
Oleg=Vip_user("Oleg",4937)
Vlad=Classic_user("Vlad",7392)

print(Oleg.speak())
print(Vlad.speak())
