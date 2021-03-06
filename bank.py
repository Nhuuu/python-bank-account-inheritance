class BankAccount(object):
  def __init__(self, balance = 0):
    self.balance = balance

  def deposit(self, amount):
    if amount > 0:
      self.balance = self.balance + amount
    else:
      return False

  def withdraw(self, amount):
    if amount < self.balance:
      self.balance = self.balance - amount
    else: 
      return False

  def accumulate_interest(self):
    self.balance = self.balance * 1.02


class ChildrensAccount(BankAccount):
  def __init__(self, balance = 0):
    super(ChildrensAccount, self).__init__(balance)

  def accumulate_interest(self):
    self.balance = self.balance + 10


class OverdraftAccount(BankAccount):
  def __init__(self, balance = 0):
    super(OverdraftAccount, self).__init__(balance)

  def withdraw(self, amount, penalty=40):
    if amount > self.balance:
      self.balance = self.balance - 40
      return False
    
  def accumulate_interest(self):
    if self.balance <= 0:
      self.balance = self.balance
      






basic_account = BankAccount()
basic_account.deposit(600)
print("Basic account has ${}".format(basic_account.balance))
basic_account.withdraw(17)
print("Basic account has ${}".format(basic_account.balance))
basic_account.accumulate_interest()
print("Basic account has ${}".format(basic_account.balance))
print()

childs_account = ChildrensAccount()
childs_account.deposit(34)
print("Child's account has ${}".format(childs_account.balance))
childs_account.withdraw(17)
print("Child's account has ${}".format(childs_account.balance))
childs_account.accumulate_interest()
print("Child's account has ${}".format(childs_account.balance))
print()

overdraft_account = OverdraftAccount()
overdraft_account.deposit(12)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.withdraw(17)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.accumulate_interest()
print("Overdraft account has ${}".format(overdraft_account.balance))
