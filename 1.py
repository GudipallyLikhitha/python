
1.class Display:
    def __init__(self):
        print("vandemataram")
#instantiate object
d=Display()
2.#program to display vandemataram 10 times
class Display:
#constructor(used to write a counter)
    def __init__(self):
        self.c=1
    def process(self):
        while self.c<=10: #here c is instant variable
            print("vandemataram #",self.c)
            self.c=self.c+1
#instantiate object
d=Display()
d.process()
3.#program to display vandemataram n times on the screen
class DisplayNTimes:
#constructor
    def __init__(self):
        self.c=1
    def accept(self):
        self.n=int(input("enter a number to display:"))
    def process(self):
        while self.c<=self.n:
            print("vandemataram",self.c)
            self.c=self.c+1
d=DisplayNTimes()
d.accept()
d.process() 
4.#program to display the numbers from 1 to n
class DisplayNumbers:
    def __init__(self):
        self.c=1
    def accept(self):
        self.n=int(input("enter n value"))
    def process(self):
        while self.c<=self.n:
            print(self.c,end=" ")
            self.c=self.c+1
d=DisplayNumbers()
d.accept()
d.process()
5.#program to display numbers in the given range
class DisplayNumbers:
    def accept(self):
        self.i=int(input("enter initial value of numbers:"))
        self.f=int(input("enter final value of numbers:"))
    def process(self):
        while self.f>=self.i:
            print(self.f,end=" ")
            self.f=self.f-1
d=DisplayNumbers()
d.accept()
d.process()
6.#program to display odd numbers in the given range
class DisplayOddNum:
    def __init__(self):
        self.c=1
    def accept(self):
        self.n=int(input("enter n value:"))
    def process(self):
        while self.c<=self.n:
            self.r=self.c%2
            if self.r!=0:
                print(self.c)
            self.c=self.c+1 
p=DisplayOddNum()
p.accept()
p.process()
7.#program to find sum of odd numbers in the given range
class DisplaySum:
    def __init__(self):
        self.sum=0
    def accept(self):
        self.i=int(input("enter initial value:"))
        self.f=int(input("enter final value:"))
    def process(self):
        print("the odd numbers are \n")
        while self.i<=self.f:
            self.r=self.i%2
            if self.r!=0:
                print(self.i)
                self.sum=self.sum+self.i
            self.i=self.i+1
    def output(self):
        print("sum=",self.sum)
d=DisplaySum()
d.accept()
d.process()
d.output()
8.#program to read a number and check whether it id divisible by 2 and 5
class Demo:
   def accept(self):
       self.n=int(input("enter n value:"))
   def process(self):
       if(self.n%2==0) and (self.n%5==0):
           print("divisible")
       else:
           print("not divisible")
d=Demo()
d.accept()
d.process()  
