class BankAccount:
    pass


class MinimumBalanceAccount(BankAccount):
    def __init__(self, minimum_balance):
        super().__init__()
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print('Sorry, minimum balance must be maintained.')
        else:
            BankAccount.withdraw(self, amount)

obj = MinimumBalanceAccount(50)