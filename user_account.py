from bank_acount import BankAcount


class User:
  def __init__(self, name, email):
    #attributes
    self.name = name
    self.email = email
    self.account = BankAcount(int_rate=0.2, checking=0, saving=0)
    #methods
  def make_deposit(self,amount, account_type):
    if account_type == "checking":
      self.account.checking += amount
    elif account_type == "saving":
      self.account.saving += amount
    return self
    # Add a make_withdrawal method to the User class
  # def make_withdrawal(self, amount):
  #   self.account.balance -= amount
  #   return self

    # Add a display_user_balance method to the User class  
  def display_user_balance(self):
      print(f"{self.name} has a balance of: {self.account.checking}")
      return self
    



rashid = User("Jama", "rash@gmail.com")
rashid.make_deposit(600, "checking").display_user_balance()