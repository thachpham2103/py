
from abc import ABC, abstractmethod

class DongVat(ABC):
    def __init__(self, ten, age):
        self.ten = ten
        self.age = age
    
    @abstractmethod
    def tieng_keu(self):
        pass

    def __str__(self):
        return f'Ten: {self.ten}, Tuoi: {self.age}'
    
class Cho(DongVat):
    def __init__(self, ten, age, soChan):
        super().__init__(ten, age)
        self.soChan = soChan

    def tieng_keu(self):
        return "Gau Gau"
    
    def __str__(self):
        return super().__str__() + f', So Chan: {self.soChan}'
    
def main():
    n= int(input("Nhap so luong dong vat:"))
    ds=[]
    for i in range(n):
        print(f"Nhap con cho thu {i+1}")
        ten= input("Nhap ten:")
        age= int(input("Nhap tuoi:"))
        soChan= int(input("Nhap so chan:"))
        cho = Cho(ten, age, soChan)
        ds.append(cho)
    for dongvat in ds:
        print(dongvat)
        print("Tieng keu:", dongvat.tieng_keu())

if __name__ == "__main__":
    main()