class asb:
    def __init__(self):
        self.a =3

    def b(self):
        self.c()
        print(self.a)
        return (2,3)

    def c(self):
        self.a = 4

temp = asb()

(a,b) = temp.b()
print(a+b)

art = "asfd"