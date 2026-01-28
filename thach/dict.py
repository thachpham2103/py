
def nhap_san_pham():
    n= int(input("Nhập số lượng phần tử của lớp:"))
    a= dict()
    for i in range (n):
        print("Nhập vào các thông tin của dict A:")
        maSP = input("Nhập vào mã SP:")
        soLuong= int(input("Nhập vào số lượng:"))
        a[maSP]= soLuong
    return a

def nhap_loai():
    m= int(input("Nhap so phần tử: "))
    b= dict()
    for j in range (m):
        print("Nhập vào thông tin của B:")
        maLoai= input("Nhập vào mã loại:")
        tenLoai= input("Nhập vào tên loai")
        b[maLoai]= tenLoai
    return b

def check(a):
    if "001" in a:
        a["001"]=9
        # return a
        print("Cập nhật thông tin thành công")
    else:
        so_luong= int(input("Nhập vào số lượng cần update:"))
        a["001"]=so_luong
        print("Cập nhật thành công!!")


def xoa_so_luong_bang_0(a):
    ds_xoa = []

    for maSP, soLuong in a.items():
        if soLuong == 0:
            ds_xoa.append(maSP)

    for maSP in ds_xoa:
        del a[maSP]

    if ds_xoa:
        print("Đã xóa các sản phẩm có số lượng = 0:", ds_xoa)
    else:
        print("Không có sản phẩm nào có số lượng = 0")

def tach_list(a):
    list1= list(a.keys())
    list2= list(a.values())

    print("Phần tử đầu danh sách:", list1[:3])
    print("Phần tử cuối danh sách:", list2[-3:])    

def main():
    a=nhap_san_pham()
    b= nhap_loai()
    check(a)
    xoa_so_luong_bang_0(a)
    tach_list(a)

if __name__=="__main__":
    main()

        