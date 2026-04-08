
from abc import ABC
class Document(ABC):
    def __init__(self, doc_id, title, base_price):
        self._doc_id = doc_id          # protected
        self.title = title             # public
        self.__base_price = base_price # private

    @property
    def base_price(self):
        return self.__base_price  # chỉ đọc

    
    def calculate_rental_fee(self, days):
        pass


# ================= PHẦN 2: KẾ THỪA =================
class PhysicalBook(Document):
    def __init__(self, doc_id, title, base_price, weight):
        super().__init__(doc_id, title, base_price)
        self.weight = weight

    def calculate_rental_fee(self, days):
        return (self.base_price * days) + (self.weight * 2)

    def __str__(self):
        return f"[PhysicalBook] - {self._doc_id} - {self.title}"


class EBook(Document):
    def __init__(self, doc_id, title, base_price, file_size):
        super().__init__(doc_id, title, base_price)
        self.file_size = file_size

    def calculate_rental_fee(self, days):
        fee = self.base_price * days
        if self.file_size > 100:
            fee += fee * 0.05  # phụ phí 5%
        return fee

    def __str__(self):
        return f"[EBook] - {self._doc_id} - {self.title}"


# ================= PHẦN 3: MEMBER =================
class InsufficientFundsError(Exception):
    pass


class Member:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Số tiền nạp không hợp lệ!")

    def pay(self, amount):
        if self.__balance < amount:
            raise InsufficientFundsError("Không đủ tiền!")
        self.__balance -= amount

    def get_balance(self):
        return self.__balance


# ================= PHẦN 4: LIBRARY MANAGER =================
class LibraryManager:
    def __init__(self):
        self.docs_list = []
        self.members_list = []

    def add_document(self, doc):
        self.docs_list.append(doc)

    def add_member(self, member):
        self.members_list.append(member)

    def find_document(self, doc_id):
        for doc in self.docs_list:
            if doc._doc_id == doc_id:
                return doc
        return None

    def rent_document(self, member, doc_id, days):
        doc = self.find_document(doc_id)

        if not doc:
            print("Không tìm thấy tài liệu!")
            return

        fee = doc.calculate_rental_fee(days)

        try:
            member.pay(fee)
            print(f"Thuê thành công: {doc}")
            print(f"Phí: {fee}")
            print(f"Số dư còn lại: {member.get_balance()}")
        except InsufficientFundsError as e:
            print(f"Lỗi: {e}")

    @staticmethod
    def is_valid_doc_id(doc_id):
        import re
        return bool(re.match(r"^LIB\d{4}$", doc_id))


# ================= TEST CASE =================
def main():
    # Tạo tài liệu
    b1 = PhysicalBook("LIB1001", "Java Basics", 10, 2)
    ebook1 = EBook("LIB2002", "Python Advanced", 8, 150)

    # Tạo member
    member = Member("Nguyen Van A", 50)

    # Tạo manager
    manager = LibraryManager()
    manager.add_document(b1)
    manager.add_document(ebook1)

    # Test 1: thuê PhysicalBook
    print("\n--- Thuê sách giấy ---")
    manager.rent_document(member, "LIB1001", 5)

    # Test 2: thuê EBook (gây lỗi)
    print("\n--- Thuê Ebook (gây lỗi) ---")
    manager.rent_document(member, "LIB2002", 100)


if __name__ == "__main__":
    main()