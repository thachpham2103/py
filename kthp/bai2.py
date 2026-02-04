class Nguoi:
    def __init__(self, name, ngaySinh, diaChi):
        self.name = name
        self.ngaySinh = ngaySinh
        self.diaChi = diaChi

    def __str__(self):
        return f'Name: {self.name}, Ngay Sinh: {self.ngaySinh}, Dia Chi: {self.diaChi}'


class GiaoVien(Nguoi):
    def __init__(self, name, ngaySinh, diaChi, monDay, trinhDo, soNamCongTac):
        super().__init__(name, ngaySinh, diaChi)
        self.monDay = monDay
        self.trinhDo = trinhDo
        self.soNamCongTac = soNamCongTac

    def __lt__(self, other):
        if not isinstance(other, GiaoVien):
            return NotImplemented
        return self.soNamCongTac < other.soNamCongTac

    def __str__(self):
        return super().__str__() + \
               f', Mon Day: {self.monDay}, Trinh Do: {self.trinhDo}, So Nam Cong Tac: {self.soNamCongTac}'
    

def sap_xep(ds):
    ds.sort(key = lambda gv: gv.soNamCongTac, reverse=True)

def ghi_file(ds, ten_file):
    with open(ten_file, "w", encoding="utf-8") as f:
        for gv in ds:
            f.write(f'{gv.name},{gv.ngaySinh},{gv.diaChi},{gv.monDay},{gv.trinhDo},{gv.soNamCongTac}\n')

def search_monhoc(ds):
    [print(sv) for sv in ds if any(mon.so_tin_chi == 3 for mon in sv.ds)]

def main():
    n = int(input("Nhap vao so Giao Vien: "))
    ds = []

    for i in range(n):
        print(f"\nNhap vao thong tin giao vien thu {i+1}")
        name = input("Ten: ")
        ngaySinh = input("Ngay sinh: ")
        diaChi = input("Dia chi: ")
        monDay = input("Mon day: ")
        trinhDo = input("Trinh do: ")
        soNamCongTac = int(input("So nam cong tac: "))

        gv = GiaoVien(name, ngaySinh, diaChi, monDay, trinhDo, soNamCongTac)
        ds.append(gv)

    print("\nSo sanh 2 giao vien dau tien:")
    if n >= 2:
        print(ds[0] < ds[1])

    print("\nDanh sach sau khi sap xep giam dan theo so nam cong tac:")
    sap_xep(ds)
    for gv in ds:
        print(gv)

    search_monhoc(ds)
    print("\nDa tim kiem xong giao vien day mon co 3 tin chi.")
    print(ds)

    ghi_file(ds, "GIAOVIEN.txt")
    print("\nDa ghi file GIAOVIEN.txt")


if __name__ == "__main__":
    main()
