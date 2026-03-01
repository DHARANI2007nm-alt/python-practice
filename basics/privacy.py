class Demo:

    def __init__(self):
        self.name = "Public variable"
        self._age = 20
        self.__marks = 95

d = Demo()
print("Outside class access:")
print(d.name)
print(d._age)
print(type(d))
print(d.__marks)
