from SinhVien import SinhVien

class QuanLySinhVien:
    def __init__(self):
        self.listSinhVien = []

    def themSinhVien(self, sv: SinhVien):
        self.listSinhVien.append(sv)

    def xuatDanhSachSinhVien(self):
        for sv in self.listSinhVien:
            sv.hienThiThongTin()

    def tinhDiemTrungBinh(self):
        for sv in self.listSinhVien:
            sv.tinhDiemTrungBinh()

    def xepLoaiHocLuc(self):
        for sv in self.listSinhVien:
            sv.xepLoaiHocLuc()

    def showSinhVien(self, listSV):
        for sv in listSV:
            sv.hienThiThongTin()

    def getSinhVienGioi(self):
        listGioi = []
        for sv in self.listSinhVien:
            if sv._hocLuc == "Gioi":
                listGioi.append(sv)
        return listGioi

    def getSinhVienTheoHocLuc(self, hocLuc):
        listSV = []
        if self.soLuongSinhVien() > 0:
            for sv in self.listSinhVien:
                if sv._hocLuc.upper() == hocLuc.upper():
                    listSV.append(sv)
        return listSV

    def sapXepTheoDiemTrungBinh(self):
        self.listSinhVien.sort(key=lambda x: x._diemTrungBinh, reverse=True)

    def sapXepTheoTen(self):
        self.listSinhVien.sort(key=lambda x: x._hoTen)

    def soLuongSinhVien(self):
        return len(self.listSinhVien)


