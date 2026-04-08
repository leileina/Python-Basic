#bài 2
print("Hello Python")
#Bài 3: Viết chương trình nhận vào một danh sách các số thực từ đối số dòng lệnh (sys.argv).
#Hiển thị số lớn nhất và tổng của danh sách.
#Sử dụng try...except để loại bỏ các phần tử không phải là số thực.
# loai bỏ các
import sys # =>vào thư viện để dung avgv
numbers = [] # => Tạo danh sách rỗng để lưu số hợp lệ

for arg in sys.argv[1:]: # =>sys.argv là danh sách:[tên_file.py, tham_số_1, tham_số_2,...]

# bỏ tên file, chỉ lấy dữ liệu người dùng nhập
    try:
        num = float(arg) # => chuyển giá trị sang số thực
        numbers.append(num) #  =>nếu thanh công thêm vào list
    except:
        pass  # bỏ qua nếu không phải số

if numbers:# nếu list ko rỗng
    print("Danh sách hợp lệ:", numbers)
    print("Số lớn nhất:", max(numbers))
    print("Tổng:", sum(numbers))
else:
    print("Không có số hợp lệ!")

#bài 4:Viết chương trình nhập vào 2 số nguyên $a$ và $b$ từ bàn phím. Tính tổng. Nếu nhập sai định dạng, yêu cầu người dùng nhập lại cho đến khi đúng.

while True:
    try:
        a = int(input("Nhập a: "))
        b = int(input("Nhập b: "))
        break # => ko lỗi thì thoát vòng lặp
    except:
        print("Nhập sai! Vui lòng nhập lại.")

print("Tổng:", a + b)

#bai 5:Viết chương trình giải phương trình bậc 2. Thiết kế gồm các hàm giai_bac_1(a, b) và giai_bac_2(a, b, c).

import math #=> vào thư viện để dùng hàm sqrt()

def giai_bac_1(a, b):
    if a == 0: #nếu ko còn x (ko phải bâc1)
    
        if b == 0: #=> nếu luôn =0 x vô số nghiệm
            print("Vô số nghiệm")
        else:
            print("Vô nghiệm")#và ngược lại
    else:
        print("Nghiệm:", -b / a)

def giai_bac_2(a, b, c):
    if a == 0:
        giai_bac_1(b, c)
        return
    
    delta = b**2 - 4*a*c# công thức
    
    if delta < 0:
        print("Vô nghiệm")
    elif delta == 0:
        print("Nghiệm kép:", -b / (2*a))
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("2 nghiệm:", x1, x2)

# Test
giai_bac_2(1, -3, 2)

#bài 6: Nhập vào 1 số nguyên. Kiểm tra số nguyên tố và hiển thị số đó dưới dạng nhị phân (bin()).
#số nguyên tố là số lớn hơn 1 và chia hết cho chính nó
def is_prime(n): #hàm ktra số nguyên
    if n < 2: #Số < 2 không phải số nguyên tố
        return False
    for i in range(2, int(n**0.5) + 1): #Lặp từ 2 → √n
                                        #tối ưu (không cần kiểm tra hết)
        if n % i == 0:
            return False
    return True

n = int(input("Nhập số nguyên: "))

if is_prime(n):
    print("Là số nguyên tố")
else:
    print("Không phải số nguyên tố")

print("Dạng nhị phân:", bin(n))

#bài 7:Nhập chuỗi họ tên. Sử dụng các phương thức xử lý chuỗi để tách và hiển thị phần Tên.

name = input("Nhập họ tên: ") #nhập chuỗi họ tên

name = name.strip().split()[-1] # Lấy chữ cuối cùng trong họ tên

print("Tên là:", name)

#bai 8: Nhập một danh sách số nguyên và một số $x$.
#Đếm số lần xuất hiện của $x$.
#Sắp xếp danh sách tăng dần và hiển thị.

# Nhập danh sách
l = list(map(int, input("Nhập danh sách số nguyên: ").split()))

x = int(input("Nhập x: "))

# Đếm
count = l.count(x)
print("Số lần xuất hiện của x:", count)

# Sắp xếp
l.sort() # sắp xếp tăg dần
print("Danh sách sau khi sắp xếp:", l)