#programs on loops
#program to find factors of the given number
#example 6=1,2,3, sum=6 perfect
#8=1,2,4,  sum=7 not perfect
#10=1,2,5 sum=8 not perfect
#28=1,2,4,7,14 sum=28 perfect
class Demo:
    def __init__(self):
        self.sum=0
    def accept(self):
        self.n=int(input("enter the value"))
    def process(self):
        while self.n>0:
            self.r=self.n%10
            self.sum=self.sum+self.r
            self.n=self.n//10
        print("sum=",self.sum)
         
d=Demo()
d.accept()
d.process()

