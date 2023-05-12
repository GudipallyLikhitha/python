'''#program to reverse the given number
class Demo:
    def __init__(self):
        self.rev=0
    def accept(self):
        self.n=int(input("enter the number"))
    def process(self):
        while self.n>0:
            self.r=self.n%10
            self.rev=self.rev*10+self.r
            self.n=self.n//10
        print(self.rev)
d=Demo()
d.accept()
d.process()
#program to check the given number is palindrome
class Demo:
    def __init__(self):
        self.rev=0
    def accept(self):
        self.n=int(input("enter the number"))
        self.num=self.n
    def process(self):
        while self.num>0:
            self.r=self.num%10
            self.rev=self.rev*10+self.r
            self.num=self.num//10
    
        if self.rev==self.n:
            print("the num is palindrome")
        else:
            print("the num is not a palindrome")
       
d=Demo()
d.accept()
d.process()
#to find the sum of the squares of the given number ex=1234,sum=1+4+9+16=30
class Demo:
    def __init__(self):
        self.sum=0
    def accept(self):
        self.n=int(input("enter n value"))
    def process(self):
        while self.n>0:
            r=self.n%10
            self.sum=self.sum+r**2
            self.n=self.n//10
        print("the sum=",self.sum)
       
d=Demo()
d.accept()
d.process()
#program to count the number of digits
    def __init__(self):
        self.c=0
    def accept(self):
        self.n=int(input("enter the value:"))
    def process(self):
        while self.n>0:
            self.c=self.c+1
            self.n=self.n//10
        print(self.c)
d=Demo()
d.accept()
d.process()
#program to evaluate b**p
class Demo:
    def __init__(self):
        self.res=1
        self.c=1
    def accept(self):
        self.b=int(input("enter the b value:"))
        self.p=int(input("enter the p value:"))
    def process(self):
        while self.c<=self.p:
            self.res=self.res*self.b
            self.c=self.c+1
        print(self.res)
d=Demo()
d.accept()
d.process()''
#program to check the given number is armstrong number or not
class Demo:
    def __init__(self):
        self.c=0
        self.sum=0
    def accept(self):
        self.n=int(input("enter the number"))
        self.num=self.n
        self.x=self.n
    def process(self):
        while self.n!=0:
            self.n=self.n//10
            self.c=self.c+1
        print("given number is a {} digit number".format(self.c))
        while self.num!=0:
            self.i=self.num%10
            self.sum=self.sum+(self.i**self.c)
            self.num=self.num//10
        if self.sum==self.x:
            print("armstrong")
        else:
            print("not armstrong")
d=Demo()
d.accept()
d.process()'''

        

        
        
        

     
    
    


            
