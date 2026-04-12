import copy

class MaTran:
    def __init__(self, hang=0, cot=0):
        self.__hang = hang
        self.__cot = cot
        # Thuộc tính private: ẩn dữ liệu ma trận
        self.__data = [[0 for _ in range(cot)] for _ in range(hang)]

    # Nhập ma trận từ bàn phím
    def input_matrix(self):
        print(f"Nhập ma trận {self.__hang}x{self.__cot}:")
        for i in range(self.__hang):
            line = input(f"Dòng {i+1} (nhập {self.__cot} số, cách nhau bởi dấu cách): ").split()
            self.__data[i] = [float(x) for x in line]

    # Hiển thị ma trận
    def display(self):
        for row in self.__data:
            print("\t".join([f"{x:.2f}" for x in row]))

    # Kiểm tra ma trận vuông
    def la_ma_tran_vuong(self):
        return self.__hang == self.__cot

    # Cộng ma trận
    def add(self, other):
        if self.__hang != other.__hang or self.__cot != other.__cot:
            raise Exception("Lỗi: Kích thước không khớp để cộng!")
        
        ket_qua = MaTran(self.__hang, self.__cot)
        for i in range(self.__hang):
            for j in range(self.__cot):
                ket_qua.__data[i][j] = self.__data[i][j] + other.__data[i][j]
        return ket_qua

    # Nhân ma trận: (m x n) * (n x p) = (m x p)
    def multiply(self, other):
        if self.__cot != other.__hang:
            raise Exception("Lỗi: Số cột ma trận đầu phải bằng số dòng ma trận sau!")
        
        ket_qua = MaTran(self.__hang, other.__cot)
        for i in range(self.__hang):
            for j in range(other.__cot):
                for k in range(self.__cot):
                    ket_qua.__data[i][j] += self.__data[i][k] * other.__data[k][j]
        return ket_qua

    # Ma trận chuyển vị
    def transpose(self):
        ket_qua = MaTran(self.__cot, self.__hang)
        for i in range(self.__hang):
            for j in range(self.__cot):
                ket_qua.__data[j][i] = self.__data[i][j]
        return ket_qua

    # NÂNG CAO: Tính định thức (Determinant) bằng đệ quy
    def determinant(self):
        if not self.la_ma_tran_vuong():
            raise Exception("Lỗi: Định thức chỉ tính được cho ma trận vuông!")
        
        # Trường hợp cơ bản 1x1 và 2x2
        if self.__hang == 1:
            return self.__data[0][0]
        if self.__hang == 2:
            return self.__data[0][0]*self.__data[1][1] - self.__data[0][1]*self.__data[1][0]

        det = 0
        for j in range(self.__cot):
            # Tạo ma trận con bằng cách bỏ dòng 0 và cột j
            con = self.__get_submatrix(0, j)
            det += ((-1) ** j) * self.__data[0][j] * con.determinant()
        return det

    # Hàm hỗ trợ lấy ma trận con (phục vụ tính định thức)
    def __get_submatrix(self, row_to_remove, col_to_remove):
        sub = MaTran(self.__hang - 1, self.__cot - 1)
        sub_data = []
        for i in range(self.__hang):
            if i == row_to_remove: continue
            new_row = [self.__data[i][j] for j in range(self.__cot) if j != col_to_remove]
            sub_data.append(new_row)
        sub.__data = sub_data
        return sub

# --- CHƯƠNG TRÌNH KIỂM TRA ---
try:
    mt1 = MaTran(2, 2)
    mt1.input_matrix()
    
    print("\nMa trận vừa nhập:")
    mt1.display()

    print(f"\nChuyển vị:")
    mt1.transpose().display()

    if mt1.la_ma_tran_vuong():
        print(f"\nĐịnh thức: {mt1.determinant()}")

except Exception as e:
    print(e)