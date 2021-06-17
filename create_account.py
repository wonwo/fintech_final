from eth_account import Account

class Create():  
  def create_new(self,key):
        ac1 = Account.create(key)
        ac1privatekey = ac1.privateKey
        return ac1privatekey.hex(),ac1.address
        