class A:
    classvar1 = 'I am a class variable of A.'

    def __init__(self):
        self.var1 = "I am in class A's constractor."
        self.classvar1 = "I am instance variable of A."
        self.special = "Special var of A."


class B(A):
    classvar1 = "I am in class B."

    def __init__(self):
        super().__init__()
        self.var1 = "I am in class B's constractor."
        self.classvar1 = "I am instance variable of B."
        print(super().classvar1)


a = A()
b = B()

print(b.special, b.var1, b.classvar1)
