
class SanPham:
    def __init__(self, ma_sp, ten, gia_ban):
        self.ma_sp = ma_sp
        self.ten = ten
        self.gia_ban = gia_ban

    def __str__(self):
        return f'Ma SP: {self.ma_sp}, Ten :{self.ten}, Gia Ban: {self.gia_ban}'
    
class DonHang:
    def __init__(self, ma_dh, nhay_lap, danh_sach_san_pham):
        self.ma_dh = ma_dh
        self.nhay_lap = nhay_lap
        self.danh_sach_san_pham = []
        # self.onj= SanPham()

    def them_san_pham(self, ma_san_pham, ten, gia_ban):
        danh_sach_san_pham= SanPham(ma_san_pham, ten, gia_ban)
        self.danh_sach_san_pham.append(danh_sach_san_pham)
    
    def tong_tien(self):
        tong=0
        for san_pham in self.danh_sach_san_pham:
            tong += san_pham.gia_ban
        return tong
    
    def __str__(self):
        return f'Ma DH: {self.ma_dh}, Nhay Lap: {self.nhay_lap}, Tong Tien: {self.tong_tien()}, Danh sach san pham: {", ".join(str(san_pham) for san_pham in self.danh_sach_san_pham)}'
    

class DonHangOnline(DonHang):
    def __init__(self, cuoc_phi, dia_chi_van_chuyen, ma_dh, nhay_lap, danh_sach_san_pham):
        super().__init__(ma_dh, nhay_lap, danh_sach_san_pham)
        self.cuoc_phi = cuoc_phi
        self.dia_chi_van_chuyen = dia_chi_van_chuyen
    
    def __tong_tien__(self):
        return super().tong_tien() +self.cuoc_phi
    
    def __str__(self):
        return super().__str__() + f', Cuoc Phi: {self.cuoc_phi}, Dia Chi Van Chuyen: {self.dia_chi_van_chuyen}'
    
    def __add__(self, other):
        if isinstance(other, DonHangOnline):
            ma_dh= self.ma_dh+ "&" + other.ma_dh
            nhay_lap= self.nhay_lap + " & " + other.nhay_lap
            danh_sach_san_pham= self.danh_sach_san_pham + other.danh_sach_san_pham
            cuoc_phi= self.cuoc_phi + other.cuoc_phi
            dia_chi_van_chuyen= self.dia_chi_van_chuyen + " & " + other.dia_chi_van_chuyen
            return DonHangOnline(cuoc_phi, dia_chi_van_chuyen, ma_dh, nhay_lap, danh_sach_san_pham)
        else:
            print("Khong the gop hai don hang online voi nhau!!!")

def main():
    n= int(input("Nhap vao so don hang:"))
    danh_sach_don_hang= []
    for i in range (n):
        print(f'Nhap thong tin cua don hang {i+1}:')
        ma_dh = input("Nhap ma don hang:")
        nhay_lap= input("Nhap nhay lap:")
        don_hang= DonHang(ma_dh, nhay_lap, [])
        m= int(input("Nhap so san pham muon them:"))
        for j in range (m):
            print(f'Nhap thong tin san pham thu {j+1}:')
            ma_san_pham= input("Nhap ma san pham:")
            ten= input("Nhap ten san pham:")
            gia_ban= float(input("Nhap gia ban san pham:"))
            don_hang.them_san_pham(ma_san_pham, ten, gia_ban)
        danh_sach_don_hang.append(don_hang)
    print("\nDanh sach don hang va san pham:")
    for don_hang in danh_sach_don_hang:
        print(don_hang) 
    don_hang1= danh_sach_don_hang[0]
    don_hang2= danh_sach_don_hang[0]
    don_hang_hop_nhat= don_hang1 and don_hang2
    print("\nDon hang hop nhat:")
    print(don_hang_hop_nhat)
    c= DonHangOnline(50000, "123 ABC", "DH001", "Ngay 1", [])
    c.them_san_pham("SP001", "San Pham 1", 100000)
    c.them_san_pham("SP002", "San Pham 2", 200000)
    print("\nThong tin don hang online:")   
    print(c)

if __name__ == "__main__":
    main()




