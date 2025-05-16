class SinhVien:
    def __init__(self, maSo="", hoTen="", diemToan=0.0, diemLy=0.0, diemHoa=0.0):
        self._maSo = maSo
        self._hoTen = hoTen
        self._diemToan = diemToan
        self._diemLy = diemLy
        self._diemHoa = diemHoa
        self._diemTrungBinh = 0.0
        self._hocLuc = ""


    def tinhDiemTrungBinh(self):
        self._diemTrungBinh = (self._diemToan + self._diemLy + self._diemHoa) / 3

    def xepLoaiHocLuc(self):
        if self._diemTrungBinh >= 8:
            self._hocLuc = "Gioi"
        elif self._diemTrungBinh >= 6.5:
            self._hocLuc = "Kha"
        elif self._diemTrungBinh >= 5:
            self._hocLuc = "Trung binh"
        else:
            self._hocLuc = "Yeu"

    def hienThiThongTin(self):
        print(f"{self._maSo:<10}{self._hoTen:<25}{self._diemToan:<10}{self._diemLy:<10}{self._diemHoa:<10}"
              f"{round(self._diemTrungBinh, 2):<10}{self._hocLuc:<15}")
