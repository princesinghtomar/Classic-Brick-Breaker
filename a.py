# import time
# class asb:
#     def __init__(self,b):
#         self.a = time.time()
#         self.b = b

#     def b(self):
#         self.c()
#         print(self.a)
#         return (2,3)

#     def c(self):
#         self.a = 4
    
#     def ptime(self):
#         print(self.a)

# class abc(asb):
#     def __init__(self):
#         asb.__init__(self,2)
#         # self.a = time.time()

#     def p(self):
#         print(self.a)
#         print("b : " + str(self.b))

# class adc(asb):
#     def __init__(self):
#         asb.__init__(self,4)
#         # self.a = 5

#     def p(self):
#         print(self.a)
#         print("b : " + str(self.b))
        

# temp = asb(2)

# temp.ptime()
# # (a,b) = temp.b()
# # print(a+b)

# # art = "asfd"

# temp1 = abc()
# temp2 = adc()

# temp1.p()
# temp2.p()

def c(l):
    l[1] = 4

def a():
    b = [3,2]
    c(b)
    print(b)

a()