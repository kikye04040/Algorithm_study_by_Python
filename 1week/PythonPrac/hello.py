# class

class Person:
    def __init__(self, name):
        self.name = name

    def sayHello(self, toWhom):
        print(f"hello, {toWhom}. I am {self.name}")

kihye = Person("기혜")
kihye.sayHello("정민")

jeongmin = Person("정민")
jeongmin.sayHello("기혜")