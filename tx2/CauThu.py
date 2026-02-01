
class CauThu:
    def __init__(self, ho_ten, vi_tri, quoc_tich):
        self.ho_ten=ho_ten
        self.vi_tri=vi_tri
        self.quoc_tich=quoc_tich

    def __str__(self):
        return f'Ho teen :{self.ho_ten}, Vi Tri:{self.vi_tri}, Quoc Tich:{self.quoc_tich}'
    

class DoiBong:
    def __init__(self, ten_doi, hlv, danh_sach_cau_thu):
        self.ten_doi= ten_doi
        self.hlv= hlv
        self.danh_sach_cau_thi=[]

    def them_cau_thu(self, ho_ten, vi_tri, quoc_tich):
        danh_sach_cau_thu= CauThu(ho_ten, vi_tri, quoc_tich)
        self.danh_sach_cau_thi.append(danh_sach_cau_thu)

    def __str__(self):
        return f'Ten doi:{self.ten_doi}, HLV: {self.hlv}, Danh sach cau thu : {", ".join(str(cau_thu) for cau_thu in self.danh_sach_cau_thi)}'
    

class DoiTuyenQuocGia(DoiBong):
    def __init__(self, ten_doi, hlv, danh_sach_cau_thu, quoc_gia):
        super().__init__(ten_doi, hlv, danh_sach_cau_thu)
        self.quoc_gia= quoc_gia
        
    def __str__(self):
        return super().__str__()+ f'Quoc Gia:{self.quoc_gia}'
    
    def __add__(self, other):
        if isinstance(other, DoiTuyenQuocGia):
            ten_doi=self.ten_doi + "&" +other.ten_doi
            hlv=self.hlv + " & " + other.hlv
            danh_sach_cau_thu=self.danh_sach_cau_thi + other.danh_sach_cau_thi
            quoc_gia=self.quoc_gia + " & " + other.quoc_gia
            return DoiTuyenQuocGia(ten_doi, hlv, danh_sach_cau_thu, quoc_gia)
        else:
            print("Khong he gop hai doi quoc gia voi nhau!!!")

def main():
    n = int(input("Nhap so doi bong muon nhap:"))
    danh_sach_doi_bong = []
    for i in range (n):
        print(f"Nhap vao doi bong thu{i+1}:")
        ten_doi= input("Nhap ten doi :")
        hlv= input("Nhap ten HLV:")
        doi_bong=DoiBong(ten_doi, hlv, [])

        m = int(input("Nhap vao so cau thu muon them"))
        for j in range (m):
            print(f"Nhap thong tin cau thu thu {j+1}")
            ho_ten= input("Nhap vao ho ten cau thu")
            vi_tri= input("Nhap vao vi tri cau thu:")
            quoc_tich= input("Nhap vao quoc tich cau thu:")
            # cau_thu= CauThu(ho_ten, vi_tri, quoc_tich)
            doi_bong.them_cau_thu(ho_ten, vi_tri, quoc_tich)
            danh_sach_doi_bong.append(doi_bong)
            DoiTuyenQuocGia(ten_doi, hlv, doi_bong.danh_sach_cau_thi, "Viet Nam")
    print("\nDanh sach doi bong va cau thu:")
    
    for doi_bong in danh_sach_doi_bong:
        print(doi_bong)
    
    doi_bong1=danh_sach_doi_bong[0]
    doi_bong2=danh_sach_doi_bong[0]
    doi_bong_hop_nhat= doi_bong1 and doi_bong2
    print("\nDoi bong hop nhat:")
    print(doi_bong_hop_nhat)

if __name__ == "__main__":
    main()
        