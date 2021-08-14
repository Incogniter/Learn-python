import datetime
import pytz


class Account:
    # in class first def should start with __init__ to avoid errors use @staticmethod
    @staticmethod
    def current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self._balance = balance
        self._trasnscation_list = [(Account.current_time(), balance)]
        print("Account credited for " + self._name)
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.show_balance()
            self._trasnscation_list.append((Account.current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            self._trasnscation_list.append((Account.current_time(), -amount))
        else:
            print("Insufficiant amount")
            self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self._balance))

    def show_transcation(self):
        for date, amount in self._trasnscation_list:
            if amount >= 0:
                trans_type = "deposit"
            else:
                trans_type = "withdraw"
                amount *= -1
            print("{} {} on (local time was at {}) ".format(amount, trans_type, date, date.astimezone()))


if __name__ == '__main__':
    abino = Account("ABINO Robilin", 0)
    abino.deposit(100000)
    abino.withdraw(5000)
    abino.show_balance()
    abino.withdraw(500000000)
    abino.show_transcation()

    sheryl = Account("Sheryl Priscilla", 1000)
    sheryl.__balance = 200  # protected
    sheryl.deposit(500)
    sheryl.withdraw(200)
    sheryl.show_transcation()
    sheryl.show_balance()
    print(sheryl.__dict__)
    sheryl._Account__balance = 20
