from abc import ABC

# 1. LỚP CƠ SỞ (KẾ THỪA + BAO GÓI)
class Payment(ABC):
    def __init__(self, amount, transaction_id):
        # Bao gói: __amount là private
        if amount < 0:
            raise ValueError("Số tiền không được âm!")
        
        self.__amount = amount
        self.transaction_id = transaction_id
        self.status = "Pending"

    # Getter để truy cập biến private
    def get_amount(self):
        return self.__amount

    # Phương thức trừu tượng (đa hình)
    def process_payment(self):
        pass

# 2. CÁC LỚP DẪN XUẤT (ĐA HÌNH)
# Thanh toán thẻ tín dụng
class CreditCardPayment(Payment):
    def __init__(self, amount, transaction_id, card_number):
        super().__init__(amount, transaction_id)
        self.card_number = card_number

    # Ghi đè phương thức
    def process_payment(self):
        total = self.get_amount() * 1.02  # +2%
        self.status = "Completed"
        print(f" Giao dịch {self.transaction_id}")
        print(f"Số tiền sau phí (2%): {total:.2f} USD")
        print(f"Trạng thái: {self.status}")


# Thanh toán ví điện tử
class EWalletPayment(Payment):
    def __init__(self, amount, transaction_id, wallet_id):
        super().__init__(amount, transaction_id)
        self.wallet_id = wallet_id

    def process_payment(self):
        total = self.get_amount()  # Không phí
        self.status = "Completed"
        print(f" Giao dịch {self.transaction_id}")
        print(f"Số tiền: {total:.2f} USD")
        print(f"Trạng thái: {self.status}")


# Thanh toán crypto
class CryptoPayment(Payment):
    def __init__(self, amount, transaction_id, wallet_address):
        super().__init__(amount, transaction_id)
        self.wallet_address = wallet_address

    def process_payment(self):
        total = self.get_amount() + 5  # phí cố định
        self.status = "Completed"
        print(f"Giao dịch {self.transaction_id}")
        print(f"Số tiền sau phí (Gas 5 USD): {total:.2f} USD")
        print(f"Trạng thái: {self.status}")



# 3. HÀM THỰC THI (ĐA HÌNH)
def execute_payment(payment_obj):
    payment_obj.process_payment()


#chạy thử
if __name__ == "__main__":
        p1 = CreditCardPayment(150, "THN011", "1234-5678-9102")
        p2 = EWalletPayment(200, "TXN002", "trhung@gmail.com")
        p3 = CryptoPayment(320, "TNN363", "0xABC123XYZ")

        execute_payment(p1)
        execute_payment(p2)
        execute_payment(p3)

    