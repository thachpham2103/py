
from abc import ABC, abstractmethod

class Nguoi:
    def __init__(self,name, age, quocTich):
        self.name = name
        self.age = age
        self.quocTich = quocTich

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}, Quoc Tich: {self.quocTich}'
    
class CLB:
    def __init__(self, tenCLB, ma, hlv, namThanhLap):
        self.tenCLB = tenCLB
        self.ma = ma
        self.hlv = hlv
        self.namThanhLap = namThanhLap
    
    def __str__(self):
        return f'Ten CLB: {self.tenCLB}, Ma: {self.ma}, HLV: {self.hlv.name}, Nam Thanh Lap: {self.namThanhLap}'
    
class CauThu(Nguoi):
    def __init__(self, ma, viTri, soAo, clb:CLB, name, age, quocTich):
        super().__init__(name, age, quocTich)
        self.ma = ma
        self.viTri = viTri
        self.soAo = soAo
        self.clb = clb
        self.danh_sach_clb = []

    def sua_thong_tin(self):
        name= input("Nhap ten cau thu can sua:")
        for name in self.danh_sach_clb:
            if name==self.name:
               self.soAo=7
               print("Da sua so ao thanh 7")
            else:
                print("Khong tim thay cau thu")

    def search_cau_thu(danh_sach_clb):
        tong=0
        for cauThu in danh_sach_clb:
            if cauThu.age<20:
                tong+=1
        return tong
    
    def __str__(self):
        return super().__str__() + f', Ma: {self.ma}, Vi Tri: {self.viTri}, So Ao: {self.soAo}, CLB: {self.clb.tenCLB}'

    
    def sap_xep(danh_sach_clb):
        danh_sach_clb.sort(key=lambda x:x.soAo, reverse=False)

    def ghi_file(self, ten_file):
        with open (ten_file, "w", encoding="utf-8") as f:
            for ct in self.danh_sach_clb:
                f.write(f"{ct.name},{ct.age},{ct.quocTich},{ct.ma},{ct.viTri},{ct.soAo},{ct.clb.tenCLB}\n")

def main():
    n= int(input("Nhap vao so cau thu:"))
    danh_sach_cau_thu=[]

    for i in range (n):
        print(f"Nhap vao thong tin cau thu thu {i+1}")
        ma= input("Nhap ma cau thu:")
        viTri= input("Nhap vi tri cau thu:")
        soAo= int(input("Nhap so ao cau thu:"))
        print("Nhap thong tin CLB cua cau thu:")
        tenCLB= input("Nhap ten CLB:")
        maCLB= input("Nhap ma CLB:")
        hlv_name= input("Nhap ten HLV:")
        namThanhLap= int(input("Nhap nam thanh lap CLB:"))
        name= input("Nhap ten cau thu:")
        age= int(input("Nhap tuoi cau thu:"))
        quocTich= input("Nhap quoc tich cau thu:")
        clb=CLB(tenCLB, maCLB, hlv_name, namThanhLap)
        cauthu=CauThu(ma,viTri, soAo, clb, name, age,quocTich)
        danh_sach_cau_thu.append(cauthu)
    print("\nDanh sach sau khi sap xep theo tuoi cau thu:")
    CauThu.sap_xep(danh_sach_cau_thu)

    danh_sach_cau_thu.ghi_file("CAUTHU.txt")
    danh_sach_cau_thu.sap_xep(danh_sach_cau_thu)
    danh_sach_cau_thu.search_cau_thu(danh_sach_cau_thu)
    danh_sach_cau_thu.sua_thong_tin(danh_sach_cau_thu)
    for ct in danh_sach_cau_thu:
        print(ct)
    
if __name__ == "__main__":
    main()
        
    

            