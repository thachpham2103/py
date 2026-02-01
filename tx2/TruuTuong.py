from abc import ABC, abstractmethod

class NhanVien(ABC):
    def __init__(self, ho_ten, ma_nhan_vien):
        self._ho_ten= ho_ten
        self._ma_nhan_vien= ma_nhan_vien

    @abstractmethod
    def tinh_luong(self):
        pass

    def __str__(self):
        return f'Ho Ten: {self._ho_ten}, Ma Nhan Vien: {self._ma_nhan_vien}'
    

class NVVP(NhanVien):
    def __init__(self, ho_ten, ma_nhan_vien, so_gio_lam):
        super().__init__(ho_ten, ma_nhan_vien)
        self.so_gio_lam= so_gio_lam

    def tinh_luong(self):
        return self.so_gio_lam*10000
    
    def __str__(self):
        return super().__str__()+ f'So gio lam:{self.so_gio_lam}, Luong: {self.tinh_luong()}'
    
class NVSX(NhanVien):
    def __init__(self, ho_ten, ma_nhan_vien, so_luong_san_pham):
        super().__init__(ho_ten, ma_nhan_vien)
        self.so_luong_san_pham= so_luong_san_pham

    def tinh_luong(self):
        return self.so_luong_san_pham*20000
    
    def __str__(self):
        return super().__str__()+ f'So luong san pham: {self.so_luong_san_pham}, Luong: {self.tinh_luong()}'
    
    def __eq__(self, other):
        if isinstance(other, NhanVien):
            return self.tinh_luong() == other.tinh_luong()
        return False
    
    def sap_xep_theo_luong(ds):
     return sorted(ds, key=lambda nv: nv.tinh_luong())
    
    def luu_file(self, ten_file="NHANVIEN.txt"):
        with open ("NHANVIEN.txt", "w", encoding="utf-8") as f:
            for nv in ds:
                f.write(str(nv)+ "\n")
    
def main():
    n= int(input("Nhap vao so nhan vien:"))
    ds=[]
    for i in range (n):
        print("Nhap vao nhan vien cần nhập là:")
        loai_nv=input("Nhap NVVP hoac NVSX:").upper()
        if loai_nv=="NVVP":
            ho_ten= input("Nhap ho ten nhan vien:")
            ma_nhan_vien= input("Nhap ma nhan vien:")
            so_gio_lam= int(input("Nhap so gio lam:"))
            nv= NVVP(ho_ten, ma_nhan_vien, so_gio_lam)
        elif loai_nv=="NVSX":
            ho_ten= input("Nhap ho ten nhan vien:")
            ma_nhan_vien= input("Nhap ma nhan vien:")
            so_luong_san_pham= int(input("Nhap so luong san pham:"))
            nv= NVSX(ho_ten, ma_nhan_vien, so_luong_san_pham)
        else:
            print("Loai nhan vien khong hop le!!!")
            continue
        ds.append(nv)

    print("\nDanh sach nhan vien vua nhap:")
    for nv in ds:
        print(nv)
    if len(ds)>=2:
        nv1= ds[0]
        nv2= ds[1]
        if nv1== nv2:
            print("\nHai nhan vien co luong bang nhau.")
        else:
            print("\nHai nhan vien khong co luong bang nhau.")  
    else:
        print("\nKhong co du nhan vien de so sanh.")
    
    sapXep= NVSX.sap_xep_theo_luong(ds)
    print("\nDanh sach nhan vien sau khi sap xep theo luong:")
    for nv in sapXep:
        print(nv)

    NVSX.luu_file(ds)
    
if __name__ == "__main__":
    main()

    
        
