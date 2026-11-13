class A:
    def eat(self):
        print("吃")
    def run(self):
        print("跑")
class B:
    def eat(self):
        print("吃的多")
    def run(self):
        print("跑的快")
class C(A,B):
    def eat(self):
        super().eat()
        B.run(self)

c=C()
c.eat()
c.run()
print(C.mro())



