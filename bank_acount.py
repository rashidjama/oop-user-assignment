class BankAcount:
  def __init__(self, int_rate=0.1, balance=0):
    self.int_rate = int_rate
    self.balance = balance

  def deposit(self, amount):
    self.balance += amount
    return self
  
  def widthdraw(self, amount):
    if self.balance - amount >= 0:
      self.balance -= amount
    else:
      print("Insufficient funds: Charging a $5 fee")
      self.balance -= amount + 5
    return self



  def display_acount_info(self):
    print(f"Balance: {self.balance}")
    return self

  def yield_interest(self):
      if self.balance > 0:
        self.balance += self.balance * self.int_rate
      return self
  


David = BankAcount()
# David.deposit(200).deposit(100).deposit(83).widthdraw(50).yield_interest().display_acount_info()

Zidan = BankAcount()
Zidan.deposit(40).deposit(60).widthdraw(120).yield_interest().display_acount_info()
  