from web3 import Web3
from eth_account import Account
import json

url = "https://ropsten.infura.io/v3/e15acf39b6cf48c3a5af30d897b4da9e"

w3 = Web3(Web3.HTTPProvider(url))

'''
private_key_A = "0x8d37eafd6953fc0d09ec77a53409e590d764d17f496bb7a74bfad79bb37fcfa9"
address_A = "0x5677Ef7312ae71Cc99435fa7B81B0978ebBC67d9"
private_key_B = "0xa2a0563a83b4d97b27a86186e1f3b74d0ca61be90bce19072110f1e3c6525756"
address_B = "0x9e47aa25A8a75c444965701605e95ac72d1aF3Cd"
'''

with open("./ABI.json", encoding='utf-8-sig') as f:
    info_json = json.load(f)
abi = info_json

contract_address = '0x9aa23ed3411a1c38669290cbebec2d5b0528127b'
Token_instance = w3.eth.contract(address = Web3.toChecksumAddress(contract_address), abi = abi)

class accounts():
    def __init__(self,privateKey,address):
        self.privateKey = privateKey
        self.address = address
    

    #券商給帳戶錢
    def issue(self, to_address, amount):
        Token_tx = Token_instance.functions.issue(to_address,amount).buildTransaction({
            'from': self.address,
            'nonce': w3.eth.getTransactionCount(self.address),
            'gas': 625842,
            'gasPrice': w3.toWei(1, 'gwei'),
            'value' : 0})

        signed = w3.eth.account.signTransaction(Token_tx, self.privateKey)

        Token_Tx_hash = w3.eth.sendRawTransaction(signed.rawTransaction)

        return Token_Tx_hash.hex()
    
    #券商更新股票價錢
    def updatePrice(self, amount):
        Token_tx = Token_instance.functions.updatePrice(amount).buildTransaction({
            'from': self.address,
            'nonce': w3.eth.getTransactionCount(self.address),
            'gas': 625842,
            'gasPrice': w3.toWei(1, 'gwei'),
            'value' : 0})

        signed = w3.eth.account.signTransaction(Token_tx, self.privateKey)

        Token_Tx_hash = w3.eth.sendRawTransaction(signed.rawTransaction)

        return Token_Tx_hash.hex()

    #券商更新股票庫存
    def updateQuantity(self, amount):
        Token_tx = Token_instance.functions.updateQuantity(amount).buildTransaction({
            'from': self.address,
            'nonce': w3.eth.getTransactionCount(self.address),
            'gas': 625842,
            'gasPrice': w3.toWei(1, 'gwei'),
            'value' : 0})

        signed = w3.eth.account.signTransaction(Token_tx, self.privateKey)

        Token_Tx_hash = w3.eth.sendRawTransaction(signed.rawTransaction)

        return Token_Tx_hash.hex()




    #投資者購買股票
    def buy(self,amount):
        Token_tx = Token_instance.functions.buy(amount).buildTransaction({
        'from': self.address,
        'nonce': w3.eth.getTransactionCount(self.address),
        'gas': 625842,
        'gasPrice': w3.toWei(1, 'gwei'),
        'value' : 0})

        signed = w3.eth.account.signTransaction(Token_tx, self.privateKey)

        Token_Tx_hash = w3.eth.sendRawTransaction(signed.rawTransaction)

        return Token_Tx_hash.hex()

    #投資者販賣股票
    def sell(self,amount):
        Token_tx = Token_instance.functions.sell(amount).buildTransaction({
        'from': self.address,
        'nonce': w3.eth.getTransactionCount(self.address),
        'gas': 625842,
        'gasPrice': w3.toWei(1, 'gwei'),
        'value' : 0})

        signed = w3.eth.account.signTransaction(Token_tx, self.privateKey)

        Token_Tx_hash = w3.eth.sendRawTransaction(signed.rawTransaction)

        return Token_Tx_hash.hex()

    def checkOwnBalance(self):
        balance = Token_instance.functions.checkOwnBalance().call({'from': self.address})
        return balance

    def checkOwnStock(self):
        myStock = Token_instance.functions.checkOwnStock().call({'from': self.address})
        return myStock

    def checkPrice(self):
        price = Token_instance.functions.checkPrice().call({'from': self.address})
        return price
    
    def checkStockQuantity(self):
        stockQuantity = Token_instance.functions.checkStockQuantity().call({'from': self.address})
        return stockQuantity
