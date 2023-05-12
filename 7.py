'''#Program to print sum of two numbers without using c=a+b
class Demo:
    def accept(self):
        self.a=int(input("Enter the value"))
        self.b=int(input("Enter the value"))
    def process(self):
        while self.b!=0:
            self.a=self.a+1
            self.b=self.b-1
        print("sum=",self.a)
d=Demo()
d.accept()
d.process()'
#Program to print difference of two numbers without using c=a-b
class Demo:
    def accept(self):
        self.a=int(input("Enter the value"))
        self.b=int(input("Enter the value"))
    def process(self):
        while self.b!=0:
            self.a=self.a-1
            self.b=self.b-1
        print("difference=",self.a)
d=Demo()
d.accept()
d.process()'
#program to print product without using *
class Demo:
    def __init__ (self):
        self.prod=0
    def accept(self):
        self.a=int(input("Enter the value"))
        self.b=int(input("Enter the value"))
    def process(self):
        while self.b!=0:
            self.prod=self.prod+self.a
            self.b=self.b-1
        print("product=",self.prod)
d=Demo()
d.accept()
d.process()''
#program nested loops
class Demo:
    def __init__(self):
        self.i=1
    def process(self):
        while self.i<=5:
            self.j=1
            while self.j<=6:
                print(self.j,end=" ")
                self.j=self.j+1
            self.i=self.i+1
            print()
d=Demo()
d.process()''
class Demo:
    def __init__(self):
        self.i=1
    def process(self):
        while self.i<=10:
            self.j=11
            while self.j>=1:
                if (self.j%2!=0):
                    print(self.j,end=" ")
                self.j=self.j-1
            self.i=self.i+1
            print()
d=Demo()
d.process()''
#program for mathematical table
class Table:
    def accept (self):
        self.i=int(input("Enter i value"))
        self.f=int(input("Enter f value"))
    def process (self):
        while self.i<=self.f:
            self.c=1
            while self.c<=10:
                self.p=self.i*self.c
                print("{}*{}={}".format(self.i,self.c,self.p))
                self.c=self.c+1
            self.i=self.i+1
d=Table()
d.accept()
d.process()''
#prime numbers
class Prime:
    def accept(self):
        self.i=int(input("Enter i value"))
        self.f=int(input("Enter f value"))
    def process(self):
        while self.i<=self.f:
            self.r=1
            self.c=2
            while self.c<=self.i/2 and self.r!=0:
                self.r=self.i%self.c
                self.c=self.c+1
            if self.r!=0:
                print(self.i)
            self.i=self.i+1
d=Prime()
d.accept()
d.process()''
#program to find sum of the digits of each number seperately in the given range
class Demo:
    def accept(self):
        self.i=int(input("Enter i value"))
        self.f=int(input("Enter f value"))
    def process(self):
        while self.i<=self.f:
            n=self.i
            sum=0
            while n!=0:
                self.r=n%10
                sum=sum+self.r
                n=n//10
            print("{},{}".format(self.i,sum))
            self.i=self.i+1
d=Demo()
d.accept()
d.process()''
#program to find reverse of each number in the given range
class Demo:
    def accept(self):
        self.i=int(input("Enter i value"))
        self.f=int(input("Enter f value"))
    def process(self):
        print("The palindrome numbers are")
        while self.i<=self.f:
            n=self.i
            rev=0
            while n!=0:
                self.r=n%10   
                rev=rev*10+self.r
                n=n//10
            if rev==self.i:
                print(self.i,end=" ")
            self.i=self.i+1
d=Demo()
d.accept()
d.process()'''
        
                
        
            
