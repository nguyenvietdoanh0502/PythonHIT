class Stack:
    def __init__(self,capacity: int):
        """
            Khoi tao stack
        """
        self.capacity=capacity
        self.ds=[]
    def isEmpty(self):
        """
            Kiem tra xem stack co dang rong
        """
        if len(self.ds)==0:
            return True
        else:
            return False
    def isFull(self):
        """
            Kiem tra xem stack co dang full
        """
        if len(self.ds)==self.capacity:
            return True
        else:
            return False
    def Pop(self) :
        """
            Loai bo top element va tra ve gia tri do
        """
        if(len(self.ds)!=0):
            return self.ds.pop()
        else:
            print('Danh sach trong')
    def Push(self,value) -> None:
        """
            Them value vao stack
        """
        if(len(self.ds)!=self.capacity):
            self.ds.append(value)
        else:
            print('Danh sach da full. Khong the them')
    def Top(self):
        """
            Lay gia tri top element cua stack
        """
        if(len(self.ds)!=0):
            return self.ds[self.capacity-1]
        else:
            print('Danh sach trong')
myStack = Stack(4)
myStack.Push(5)
myStack.Push(10)
myStack.Push(20)
myStack.Push(30)
print(myStack.isEmpty())
print(myStack.isFull())
print(myStack.Top())
print(myStack.Pop())
print(myStack.Push(40))
print(myStack.Pop())