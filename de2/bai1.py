
def nhap_san_pham():
    n=int(input("Nhap vao dict co {n} phan tu:"))
    a= dict()
    for i in range (n):
        maSP=input("Nhap vao mã SP:")
        soLuong=int(input("Nhap vao so luong SP:"))
        a[maSP]=soLuong
    return a
def nhap_loai_san_pham():
    m= int(input("Nhap vao dict co {m} phan tu:"))
    b= dict()
    for j in range (m):
        maLoaiSP=input("Nhap vao mã loại SP:")
        tenLoaiSP=input("Nhap vao tên loại SP:")
        b[maLoaiSP]=tenLoaiSP 
    return b

def xuat(a,b) :
    print("\n--------------------- THÔNG TIN SẢN PHẨM ---------------------")
    print("{:<15}|{:>15}".format("Mã SP", "Số lượng"))
    print("-" * 30)
    for maSP, soLuong in a.items():
        print("{:<15}|{:>15}".format(maSP, soLuong))

    print("\n--------------------- THÔNG TIN LOẠI SẢN PHẨM ---------------------")
    print("{:<15}|{:>25}".format("Mã loại SP", "Tên loại SP"))
    print("-" * 40)
    for maLoaiSP, tenLoaiSP in b.items():
        print("{:<15}|{:>25}".format(maLoaiSP, tenLoaiSP))

def check_sp(a):
    maSP_check=input("Nhap vao mã SP cần kiểm tra:")
    if maSP_check in a:
        a["soLuong"]=100
    else:
        a[maSP_check]=50
    return a

def delete(a,soLuong):
    if a[soLuong]==0:
        del a[soLuong]
    else:
        print("Rỗng")
    return a

def chuyen_dict(a):
    ma=list(a.keys())
    sl=list(a.values())
    return ma, sl

def main():
    a= nhap_san_pham()
    b= nhap_loai_san_pham()
    xuat(a,b)
    a= check_sp(a)
    print("\nSau khi kiểm tra mã SP:")
    xuat(a,b)
    a= delete(a)
    print("\nSau khi xóa sản phẩm có số lượng 0:")
    xuat(a,b)
    ma, sl= chuyen_dict(a)
    print("\nChuyển dict sang 2 list:")
    print("Mã SP:", ma)
    print("Số lượng:", sl)
if __name__ == "__main__":
    main()