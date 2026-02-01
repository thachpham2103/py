
class DoiBong:
    def __init__(self, ma, quoc_gia, lien_doan, so_lan_tham_du, thanh_tich):
        self._ma = ma
        self._quoc_gia = quoc_gia
        self._lien_doan = lien_doan
        self._so_lan_tham_du = so_lan_tham_du
        self._thanh_tich = thanh_tich

    def da_vo_dich(self):
        return self._thanh_tich.lower() == "vô địch"

    def to_row(self):
        return f"{self._ma:<5}{self._quoc_gia:<12}{self._lien_doan:<12}{self._so_lan_tham_du:<10}{self._thanh_tich:<15}"


class BangDau:
    def __init__(self, ten_bang, giai_dau, to_chuc, ngay_khai_mac, chu_nha):
        self._ten_bang = ten_bang
        self._giai_dau = giai_dau
        self._to_chuc = to_chuc
        self._ngay_khai_mac = ngay_khai_mac
        self._chu_nha = chu_nha
        self._ds_doi = []  

    
    def them_doi(self, doi: DoiBong):
        self._ds_doi.append(doi)

    def sua_chu_nha(self, chu_nha_moi):
        self._chu_nha = chu_nha_moi

    def sap_xep_giam_theo_so_lan(self):
        self._ds_doi.sort(key=lambda d: d._so_lan_tham_du, reverse=False)

    def hien_thi(self):
        print( "             "+"\nVÒNG CHUNG KẾT CÚP BÓNG ĐÁ THẾ GIỚI")
        print("         " +           self._ten_bang+"                ")
        print(f"Giải đấu: {self._giai_dau}"+"                " + f"Tổ chức: {self._to_chuc}")
        print(f"Ngày khai mạc: {self._ngay_khai_mac}"+"        " + f"Chủ nhà: {self._chu_nha}")
        # print(f"Chủ nhà: {self._chu_nha}")
        print("-" * 65)
        print(f"{'Mã':<5}{'Quốc gia':<12}{'Liên đoàn':<12}{'Số lần':<10}{'Thành tích':<15}")
        print("-" * 65)
        for doi in self._ds_doi:
            print(doi.to_row())
        print("-" * 65)

    def ghi_file(self, ten_file="BANGA.TXT"):
        with open(ten_file, "w", encoding="utf-8") as f:
            f.write("VÒNG CHUNG KẾT CÚP BÓNG ĐÁ THẾ GIỚI\n")
            f.write(self._ten_bang + "\n")
            f.write(f"{'Mã':<5}{'Quốc gia':<12}{'Liên đoàn':<12}{'Số lần':<10}{'Thành tích':<15}\n")
            for doi in self._ds_doi:
                f.write(doi.to_row() + "\n")


def main():
    print("NHẬP THÔNG TIN BẢNG ĐẤU")
    ten_bang = input("Tên bảng: ")
    giai_dau = input("Giải đấu: ")
    to_chuc = input("Tổ chức: ")
    ngay_khai_mac = input("Ngày khai mạc: ")
    chu_nha = input("Chủ nhà: ")

    bang = BangDau(ten_bang, giai_dau, to_chuc, ngay_khai_mac, chu_nha)

    n = int(input("\nNhập số lượng đội: "))
    for i in range(n):
        print(f"\nNhập đội bóng thứ {i + 1}:")
        ma = input("Mã đội: ")
        quoc_gia = input("Quốc gia: ")
        lien_doan = input("Liên đoàn: ")
        so_lan = int(input("Số lần tham dự: "))
        thanh_tich = input("Thành tích tốt nhất: ")

        doi = DoiBong(ma, quoc_gia, lien_doan, so_lan, thanh_tich)
        bang.them_doi(doi)   

    bang.sua_chu_nha("Qatar")

    # sắp xếp giảm dần theo số lần tham dự
    bang.sap_xep_giam_theo_so_lan()

    # hiển thị
    bang.hien_thi()

    # ghi file
    bang.ghi_file()
    print("\n Đã lưu dữ liệu vào file BANGA.TXT")


if __name__ == "__main__":
    main()
