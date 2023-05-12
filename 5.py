'''class Demo:
    def __init__(self):
        self.c=2
        self.r=1
    def accept(self):
        self.n=int(input("enter n value:"))
    def process(self):
        while self.c<=self.n/2 and self.r!=0:
            self.r=self.n%self.c
            self.c=self.c+1
        if self.r!=0:
            print(str(self.n)+ " is a prime number")
        else:
            print(str(self.n)+ " is not a prime number")
d=Demo()
d.accept()
d.process()''
#program to find gcd of two numbers
class Demo:
    def accept(self):
        self.a=int(input("enter a value"))
        self.b=int(input("enter b value"))
    def process(self):
        while self.a!=self.b:
            if self.a>self.b:
                self.a=self.a-self.b
            else:
                self.b=self.b-self.a
        print(self.a)
d=Demo()
d.accept()
d.process()'''
    
