from web3 import Web3
from eth_account import Account
import json

url = "https://goerli.infura.io/v3/9e6401388c364a918f27b5bf88cf83dd"

w3 = Web3(Web3.HTTPProvider(url))

with open("./ABI.json", encoding='utf-8-sig') as f:
    info_json = json.load(f)
abi = info_json

contract_address = '0x85e1b9cEEC2cF76956Ca794F730eD01bDDb61Db3'
Token_instance = w3.eth.contract(address = Web3.toChecksumAddress(contract_address), abi = abi)

class accounts():
    def __init__(self,privateKey,address):
        self.privateKey = privateKey
        self.address = address
    

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
    
    # update price
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

    # update quantity
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


    # buy
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

    # sell
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

    def checkAddressBalance(self, to_address):
        Balance = Token_instance.functions.checkAddressBalance(to_address).call({'from': self.address})
        return Balance

    def checkAddressQunatity(self, to_address):
        quantity = Token_instance.functions.checkAddressQunatity(to_address).call({'from': self.address})
        return quantity

    def checkPrice(self):
        price = Token_instance.functions.checkPrice().call({'from': self.address})
        return price
    
    def checkStockQuantity(self):
        stockQuantity = Token_instance.functions.checkQuantity().call({'from': self.address})
        return stockQuantity
