'''#program gcd
class Demo:
    def __init__(self):
        pass
    def accept(self):
        self.a=int(input("enter the value:"))
        self.b=int(input("enter the value:"))
    def process(self):
        while self.b!=0:
            self.r=self.a%self.b
            self.a=self.b
            self.b=self.r
        print("GCD:",self.a)
d=Demo()
d.accept()
d.process()''
#program for fibanocci series
class Fibanocci:
    def __init__ (self):
        self.a=0
        self.b=1
        self.c=1
    def process(self):
        while self.c<=100:
            print(self.a,end=' ')
            self.c=self.a+self.b
            self.a=self.b
            self.b=self.c
        print(self.a)
d=Fibanocci()
d.process()''
#program for n fibanocci series
class Demo:
    def __init__ (self):
        self.i=1
        self.a=0
        self.b=1
    def accept(self):
        self.n=int(input("enter the value:"))
    def process(self):
        while self.i<=self.n:
            print(self.a,end=' ')
            self.c=self.a+self.b
            self.a=self.b
            self.b=self.c
            self.i=self.i+1
d=Demo()
d.accept()
d.process()''
#program to print sum of series 1+(1/2)+.....+(1/n)
class Demo:
    def __init__ (self):
        self.i=1
        self.sum=0
    def accept(self):
        self.n=int(input("enter the number:"))
    def process(self):
        while self.i<=self.n:
            if self.i%2==0:
                self.sum=self.sum-(1/self.i)
                print('-','1/',self.i,end=' ')
            else:
                self.sum=self.sum+(1/self.i)
                print('+','1/',self.i,end=' ')
            self.i=self.i+1
        print("\nsum=",self.sum)
d=Demo()
d.accept()
d.process()''

#program to print sum of factorials
class Seriestest:
    def __init__ (self,n):
        self.n=n
    def factorial (self,n):
        fact=1
        for i in range(1,self.n+1):
            fact=fact*i
        return(fact)
    def process(self):
        sum=1
        for i in range(1,self.n+1):
            sum=sum+(i/self.factorial(i))
        return(sum)
n=int(input("enter n value:"))
d=Seriestest(n)
result=d.process()
print(result)'''
            
        
            
        
