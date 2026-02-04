
def khoi_tao_mon_hoc():
    n=int(input("Nhap vao so mon hoc:"))
    a= dict()

    if(n<5):
        print("So luong mon hoc phai lon hon bang 5")

    else:
        for i in range (n):
            print(f'Nhap thong tin mon hoc thu {i+1}')
            maMh= input("Nhap ma mon hoc:")
            tenMh= input("Nhap ten mon hoc:")
            soTinChi= int(input("Nhap so tin chi:"))
            hocKy= int(input("Nhap ao so hoc ky:"))
            giangVien= input("Nhap vao ginag vien:")
            a[maMh]=[tenMh, soTinChi, hocKy, giangVien]

    return a    

def them_mon_hoc(ds_mon):

    maMh= input("Nhap ma mon hoc can them:")
    tenMh= input("Nhap ten mon hoc can them:")
    soTinChi= int(input("Nhap so tin chi can them:"))
    hocKy= int(input("Nhap ao so hoc ky can them:"))
    giangVien= input("Nhap vao ginag vien can them:")
    ds_mon[maMh]=[tenMh, soTinChi, hocKy, giangVien]

def nhap_so_dang_ky(maMh, ds_mon):
    sinhVien= int(input("Nhap so luong sinh vien dang ky mon hoc:"))

    if maMh in ds_mon:
        ds_mon[maMh].append(sinhVien)
    else:
        print("Ma mon hoc khong ton tai")

def kiem_tra_dang_ky(maMh, ds_mon):
    if maMh in ds_mon:
        if len(ds_mon[maMh])>5:
            print("Mon hoc da du Sl dang ky")

        else:
            print("Mon hoc con cho dang ky")
    else:
        print("Ma mon hoc khong ton tai")

def search_mon_hoc(ds_mon):
    ma= input("Nhap ten giang vien can tim:")
    if ma in ds_mon:
        print("Tìm thấy tên giang vien")
        ds_mon[ma]=["A"]
    else:
        print("Khong tim thay ten giang vien")

def search_mon_hoc_tin_chi_max(ds_mon):
    max_tin_chi=ds_mon[0][2]
    for mon in ds_mon:
        if mon[2]>max_tin_chi:
            max_tin_chi=ds_mon[2]
    print(f'Mon hoc co so tin chi lon nhat la: {max_tin_chi}')

def xoa_mon_tin_chi_lon_nhat(ds_mon):
    ma_xoa = max(ds_mon, key=lambda ma: ds_mon[ma][2])
    del ds_mon[ma_xoa]

def tach_dict(ds_mon):
    list1= list(ds_mon.keys())
    list2= list(ds_mon.values())
    
    print("3 phần tử đầu:", list1[:3])
    print("3 phần tử cuối:", list2[-3:])

def sap_xep_tang(ds):
    return dict(sorted(ds.items(), key=lambda x: x[1][1]))

def sap_xep_giam(ds):
    return dict(sorted(ds.items(), key=lambda x: x[1][1], reverse=True))

def main():
    ds_mon=khoi_tao_mon_hoc()
    print(ds_mon)
    maMh=input("Nhap ma mon hoc can dang ky:")
    nhap_so_dang_ky(maMh, ds_mon)
    print(ds_mon)
    kiem_tra_dang_ky(maMh, ds_mon)
    search_mon_hoc(ds_mon)
    print(ds_mon)

    tong_dang_ky=0
    for mon in ds_mon.values():
        if len(mon)==5:
            tong_dang_ky+=mon[4]
    print(f'Tong so luong dang ky cua tat ca mon hoc la: {tong_dang_ky}')

    search_mon_hoc_tin_chi_max(ds_mon)
    xoa_mon_tin_chi_lon_nhat(ds_mon)
    print("Danh sach mon hoc sau khi xoa mon co so tin chi lon nhat:")
    print(ds_mon)

    tach_dict(ds_mon)

if __name__ == "__main__":
    main()
