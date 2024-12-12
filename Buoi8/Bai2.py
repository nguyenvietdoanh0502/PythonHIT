class person:
    def __init__(self,name:str,yob:int):
        """
            Khoi tao person
            name: Ten
            Yob: Ngay sinh
        """
        self.name=name
        self.yob=yob
    def intt(self) -> None:
        """
            In ra thong tin Person
        """
        print(f'Name: {self.name} - YoB: {self.yob}',end='')
    def getAge(self)->int:
        """
            Tra ve nam sinh
        """
        return self.yob
class Student(person):
    role='Student'
    def __init__(self, name:str, yob:int,grade:str):
        """
            Khoi tao Student
        """
        super().__init__(name, yob)
        self.grade=grade
    def intt(self) -> None:
        """
            In ra thong tin Student
        """
        print(f'{self.role} - ',end='')
        super().intt()
        print(f' - Grade: {self.grade}')
    def getRole(self) -> str:
        return self.role
class Teacher(person):
    role='Teacher'
    def __init__(self, name:str, yob:int,subject:str):
        """
            Khoi tao Teacher
        """
        super().__init__(name, yob)
        self.subject=subject
    def intt(self) -> None:
        """
            In ra thong tin Teacher
        """
        print(f'{self.role} - ',end='')
        super().intt()
        print(f' - Subject: {self.subject}')
    def getRole(self) -> str:
        return self.role
class Doctor(person):
    role='Doctor'
    def __init__(self, name:str, yob:int,specialist:str):
        """
            Khoi tao Doctor
        """
        super().__init__(name, yob)
        self.specialist=specialist
    def intt(self) -> None:
        """
            In ra thong tin Doctor
        """
        print(f'{self.role} - ',end='')
        super().intt()
        print(f' - Subject: {self.specialist}')
    def getRole(self) -> str:
        return self.role
from typing import List
class Ward:
    def __init__(self,name:str,danhsach: List):
        """
            Ham khoi tao Ward
        """
        self.name=name
        self.danhsach=danhsach
    def addPerson(self,X: person):
        """
            Them nguoi vao Ward
        """
        if(X!=None):
            self.danhsach.append(X)
        else:
            print("Du lieu khong hop le!")
    def describe(self) -> None:
        """
            In ra thong tin Ward
        """
        print(f"Name: {self.name}")
        for i in self.danhsach:
            i.intt()
    def countDoctor(self) -> int:
        """
            Dem so luong bac si
        """
        check=0
        for i in self.danhsach:
            if i.getRole()=='Doctor':
                check+=1
        return check
    def sortAge(self):
        """
            Ham sap xep tuoi tang dan
        """
        self.danhsach.sort(key=lambda person: person.yob, reverse=True)
    def aveTeacherYearOfBirth(self) -> float:
        """
            Tinh trung binh nam sinh Teacher
        """
        check=0
        sum=0
        for i in self.danhsach:
            if i.getRole()=='Teacher':
                check+=1
                sum+=i.getAge()
        return sum/check
A = Doctor('Doanh',2005,'Y Khoa')
E = Doctor('Hoang',1998,'Nha Si')
B = Teacher('Hung',2004,'Python')
F = Teacher('Nam',2000,'C++')
D = Student('Hieu',2006,'10')
lst=[]
C = Ward('Ward1',lst)
C.addPerson(A)
C.addPerson(B)
C.addPerson(D)
C.addPerson(E)
C.addPerson(F)
C.describe()
C.sortAge()
C.describe()
print(f'Trung binh nam sinh: {C.aveTeacherYearOfBirth()}')
print('So luong bac si la: ',C.countDoctor())