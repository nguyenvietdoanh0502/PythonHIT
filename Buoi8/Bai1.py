class Manufacturer:
    def __init__(self,identity: int ,location: str):
        """
            Khoi tao nha san xuat
            identity: Ma nha san xuat
            location: Vi tri nha san xuat
        """
        self.identity=identity
        self.location=location
    def describe(self) -> None:
        """
            In ra thong tin nha san xuat
        """
        print(f'Identity: {self.identity} - Location: {self.location}')
class Device(Manufacturer):
    def __init__(self,name: str,price:float, identity: int,  location: str  ):
        """
            Khoi tao thiet bi
            Name: Ten thiet bi
            Price: Gia thiet bi
        """
        super().__init__(identity, location)
        self.name=name
        self.price=price
    def describe(self) -> None:
        """
            In ra cac thong tin cua thiet bi
        """
        print(f'Name: {self.name} - Price: {self.price}')
        super().describe()
Phone = Device('Mouse',2.5,9725,"VietNam")
Phone.describe()