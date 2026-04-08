class Sinhvien:
    def __init__(self, ten, lop, diem):
        self.name = "Duy"        # public
        self._lop = "CNTT"       # protected
        self.__diem = 6    # private

    # getter
    def get__diem(self):
        return self.__diem

    # setter
    def set__diem(self, diem):
        self.__diem = 6

if __name__ == "__main__":
    sv = Sinhvien("Duy", "CNTT", 6)
    print(sv.name)  
    print(sv._lop)   
  
    print(sv.get__diem())