'''Menu driven program with the following options
1.create #self is an instant variable
2.display
3.insert
4.delete
5.exit. accept your choice and perform the operations accordingly
#can insert node at the 3 places of a linkedlist,at first node,last node and anywhere other
than at first and last''
#declaration of a node
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def create(self):
        while True:
            data=int(input("enter the number 0 to quit"))
            if data==0:
                break
            if self.head==None:
                self.head=Node(data)
                left=self.head
            else:
                right=Node(data)
                #establish link bw left and right by assigning address of right to left
                left.next=right
                left=right
    def display(self):
        left=self.head
        print("elements of the linkedlist:")
        while left!=None:
            print(left.data,end='->')
            left=left .next
        print(None)
    def insert(self):
        while True:
            print("1.insert as first node")
            print("2.insert as last node")
            print("3.insert anywhere except first and last node")
            print("4.back to main menu")
            choice=int(input("enter your choice"))
            if choice==1:
                data=int(input("enter the number to insert"))
                temp=Node(data)
                #establish link bw temp and head by assigning head to temp
                temp.next=self.head
                head=temp
                print("node inserted")
            elif choice==2:
                left=self.head
                while left.next!=None:
                    left=left.next
                data=int(input("enter the element"))
                temp=Node(data)
                left.next=temp
                print("node inserted")
            elif choice==3:
                print("insert anywhere except first and last node")
                left=self.head
                num=int(input("enter the number, after which you want to insert:"))
                while left.data!=num and left!=None:
                    left=left.next
                    if left.data==num:
                         data=int(input("enter the element to insert:"))
                         temp=Node(data)
                         right=left.next
                         left.next=temp
                         temp.next=right
                         print("data inserted")
                    else:
                        print(num,"num not found")
            else:
                return
    def delete(self):
        pass
                          
#Main
obj=LinkedList()
while True:
    print("1.create")
    print("2.display")
    print("3.insert")
    print("4.delete")
    print("5.exit")
    choice=int(input("enter your choice"))
    if choice==1:
        obj.create()
    elif choice==2:
        obj.display()
    elif choice==3:
        obj.insert()
    elif choice==4:
        obj.delete()
    else:
        break'''
        
               
                


        
        
        
