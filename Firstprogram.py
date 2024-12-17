from abc import ABC , abstractmethod
class FundTranser(ABC):
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.balance=balance

    def validate(self,amount):
        return amount<=self.balance and\
        amount>0 and len(str(self.account_number))==10
    
    @abstractmethod
    def tranfser(self,amount):
        pass

class NEFTTransfer(FundTranser):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

    def tranfser(self, amount):
        if(super().validate(amount)):
            self.balance-=amount
        else:
            print('check the amount you entered')
        print('your current balance : ',self.balance)
    
    def display_balance(self):
        print('your current balance is : ',self.balance)


ne=NEFTTransfer(9362456123,123456)
ne.display_balance()
ne.tranfser(123)
