class Demo:

    def __init__(self):
        self.name = "Public variable"
        self._age = 20
        self.__marks = 95

d = Demo()

print("Outside class access:")

# 1. Normal variable
print(d.name)

# 2. Single underscore (still accessible)
print(d._age)

# 3. Double underscore (not directly accessible)
# print(d.__marks)   ❌ This will give error

# 4. Access hidden variable (Python renames it internally)
print(type(d))
print(d.__marks)

# 5. Special method
print(type(d))
