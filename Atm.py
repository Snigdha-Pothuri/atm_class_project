class Atm(object):
    def __init__(self,cardNumber,pinNumber):
        self.cardNumber=cardNumber
        self.pinNumber=pinNumber
    def cashWithdrawal(self):
        print("Cash Withdrawal")
    def BalanceEnquiry(self):
        print("Balance Enquiry") 
example=Atm("12345","500504")
print(example.cashWithdrawal())
print(example.BalanceEnquiry())
