'''#program to find the factorial of the given number by using for loop
class Demo:
    def __init__(self):
        self.fact=1
    def accept(self):
        self.n=int(input("enter n value:"))
    def process(self):
        for i in range(1,self.n+1):
            self.fact=self.fact*i
        print("factorial:",self.fact)
d=Demo()
d.accept()
d.process()''
#program to display given mathematical table
class Demo:
    def __init__(self):
        self.c=1
    def accept(self):
        self.n=int(input("enter n value:"))
    def process(self):
        while self.c<=10:
            r=self.n*self.c
            print("{}*{}={}".format(self.n,self.c,r))
            self.c=self.c+1
d=Demo()
d.accept()
d.process()'''

