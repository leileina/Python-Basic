class BankAccount:
    def __init__(self, account_id, owner_name, balance):
        self.account_id = account_id
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        pass

    def show_info(self):
        print("Mã TK:", self.account_id)
        print("Chủ TK:", self.owner_name)
        print("Số dư:", self.balance)
        print("-----------------")


class SavingAccount(BankAccount):
    def __init__(self, account_id, owner_name, balance, interest_rate):
        super().__init__(account_id, owner_name, balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        if amount > self.balance:
            print("Không đủ tiền")
        else:
            self.balance -= amount

    def calculate_interest(self):
        return self.balance * self.interest_rate


class CheckingAccount(BankAccount):
    def __init__(self, account_id, owner_name, balance, overdraft_limit):
        super().__init__(account_id, owner_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
        else:
            print("Vượt quá hạn mức thấu chi")


class FeeAccount(BankAccount):
    def __init__(self, account_id, owner_name, balance, withdraw_fee):
        super().__init__(account_id, owner_name, balance)
        self.withdraw_fee = withdraw_fee

    def withdraw(self, amount):
        total = amount + self.withdraw_fee
        if total > self.balance:
            print("Không đủ tiền")
        else:
            self.balance -= total


acc1 = SavingAccount("TK01", "Duy", 1000000, 0.05)
acc2 = CheckingAccount("TK02", "Bình", 5000000, 200000)
acc3 = FeeAccount("TK03", "Huỳnh", 700000, 10000)

accounts = [acc1, acc2, acc3]

money = float(input("Nhập số tiền muốn rút: "))

for acc in accounts:
    acc.withdraw(money)
    acc.show_info()