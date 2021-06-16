from web3 import Web3
from eth_account import Account
import json

url = "https://ropsten.infura.io/v3/e15acf39b6cf48c3a5af30d897b4da9e"

w3 = Web3(Web3.HTTPProvider(url))

with open("./ABI.json", encoding='utf-8-sig') as f:
    info_json = json.load(f)
abi = info_json

contract_address = '0x8a6c13614c3e60d8622b2af2ea9a13a5a6ad1662'
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
            'gasPrice': w3.toWei(100, 'gwei'),
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
            'gasPrice': w3.toWei(100, 'gwei'),
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
            'gasPrice': w3.toWei(100, 'gwei'),
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
        'gasPrice': w3.toWei(100, 'gwei'),
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
        'gasPrice': w3.toWei(100, 'gwei'),
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
