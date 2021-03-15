class asb:
    def __init__(self):
        self.a =3

    def b(self):
        self.c()
        print(self.a)

    def c(self):
        self.a = 4

temp = asb()

temp.b()
