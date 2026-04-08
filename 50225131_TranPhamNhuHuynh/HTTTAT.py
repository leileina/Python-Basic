# ===== CLASS GỐC =====
class PaymentProcess:
    def process(self, amount):
        print(f"Thanh toán: {amount}")


# ===== DECORATOR CHA =====
class PaymentDecorator(PaymentProcess):
    def __init__(self, payment):
        self.payment = payment  # đối tượng được bọc


# ===== LOGGING =====
class LoggingDecorator(PaymentDecorator):
    def process(self, amount):
        print("Ghi log giao dịch...")
        self.payment.process(amount)


# ===== OTP =====
class SmsAuthDecorator(PaymentDecorator):
    def process(self, amount):
        otp = input("Nhập OTP: ")
        if otp == "123":
            self.payment.process(amount)
        else:
            print("OTP sai!")


# ===== DISCOUNT =====
class DiscountDecorator(PaymentDecorator):
    def process(self, amount):
        print("Giảm 10% vì ngày lễ")
        amount *= 0.9
        self.payment.process(amount)
#TEST
payment = PaymentProcess()
# xếp chồng decorator
payment = LoggingDecorator(payment)
payment = SmsAuthDecorator(payment)
payment = DiscountDecorator(payment)

payment.process(100)