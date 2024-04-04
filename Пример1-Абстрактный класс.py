from abc import ABC, abstractmethod

class Robot(ABC):
    def __init__(self, model, author):
        self.model = model
        self.author = author

    @abstractmethod
    def get_result(self):
        pass

class Helicopter(Robot):
    def get_result(self):
        print(f'"{self.model}" - летающий прототип, автор - {self.author}')

class Car(Robot):
    def get_result(self):
        print(f'"{self.model}" - ездующая модель, автор - {self.author}')

class Poetry(Robot):
    pass

Helicopter_Robot = Helicopter("4282UP", "Bob1")
Car_Robot = Car("582Вездеход", "Bob2")
Helicopter_Robot.get_result()
Car_Robot.get_result()