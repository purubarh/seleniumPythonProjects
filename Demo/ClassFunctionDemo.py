class MyClass:
    name = "Arnavi"

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def sum(self, a, b):
        print(a + b)


x = MyClass()
print(x.name)
x.sum(10, 20)
