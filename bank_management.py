# main menu
# 1. new account
# 2. deposit amount
# 3. withdraw amount
# 4. balance enquiry
# 5. all acount holder list
# 6. close account
# 7. exit




# openning ann account
class Account:
    acc_no = 0
    name_acc_holder = 0
    deposit = 0
    type = 0
    def new_account(self):
        self.acc_no = int(input("Enter the new account number:"))
        self.name_acc_holder=input("Enter the name of the account holder:").upper()
        self.type=input("Enter which type of account you want to open Current or Saving [C/S]:").upper()
        self.deposit = input("Enter the amount you want to deposit:")