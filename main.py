import time
from web3 import Web3, HTTPProvider

with open("secrets/infura.api")  as file: api = file.read().strip()
with open("secrets/public.key")  as file: public = file.read().strip()
with open("secrets/private.key") as file: private = file.read().strip()

w3 = Web3(HTTPProvider(api))

balance = w3.eth.get_balance(public)
print(balance)
print(w3.eth.accounts)

