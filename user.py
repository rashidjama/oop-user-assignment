class User:
  def __init__(self, name, email):
    #attributes
    self.name = name
    self.email = email
    self.balance =0
    #methods
  def make_deposit(self, amount):
    self.balance += amount
  def make_withdrawal(self, amount):
    self.balance -= amount;
  def display_user_balance(self):
    print(f"Balance: {self.balance}")
  def transfer_money(self, amount):
    john.make_withdrawal(amount)
    doe.make_deposit(amount)

john = User("John", "john@gmail.com")

john.make_deposit(500)
john.make_deposit(700)
john.make_deposit(2000)

# john.display_user_balance()

jane = User("Jane", "jane@hotmail.com")

jane.make_deposit(1200)
jane.make_deposit(300)

jane.make_withdrawal(400)
jane.make_withdrawal(100)

# jane.display_user_balance()


doe = User("Doe", "doe@yahoo.com")

doe.make_deposit(5000)

doe.make_withdrawal(4000)
doe.make_withdrawal(300)
doe.make_withdrawal(300)

# doe.display_user_balance()

#Transfer money
john.transfer_money(1200)

# doe.display_user_balance()
# john.display_user_balance()

