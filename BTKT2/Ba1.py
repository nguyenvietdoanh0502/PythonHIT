class Stack:
    """
        Xay dung lop Stack
    """
    def __init__(self,capacity:int)->None:
        """
            Dung de khoi tao stack
            Capacity: so luong element ma stack co the chua
        """
        self.capacity=capacity
        self.stack=[]
    def isEmpty(self)->bool:
        """
            Dung de kiem tra xem stack co trong hay khong
        """
        if(len(self.stack)==0):
            return True
        else:
            return False
    def isFull(self)->bool:
        """
            Dung de kiem tra xem stack co full hay khong
        """
        if(len(self.stack)==self.capacity):
            return True
        else:
            return False
    def pop(self)->int:
        """
            Loai bo top element va tra ve gia tri do
        """
        if(self.isEmpty()):
            print('Stack trong, khong the thuc hien lenh pop')
        else:
            return self.stack.pop()
    def push(self,value:int):
        """
            Them vao stack gia tri value
        """
        if(self.isFull()):
            print('Stack da full, khong the them gia tri')
        else:
            self.stack.append(value)
    def top(self)->int:
        """
            Tra ve gia tri top element hien tai cua stack nhung khong loai bo gia tri do
        """
        if(self.isEmpty()):
            print('Khong the thuc hien do danh sach trong')
        else:
            return self.stack[len(self.stack)-1]
stack1 = Stack(capacity=5)
stack1.push(1)
stack1.push(2)
print(stack1.isFull())
print(stack1.top())
print(stack1.pop())
print(stack1.top())
print(stack1.pop())
print(stack1.isEmpty())
