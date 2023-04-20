from web3 import Web3
import time
from logger import Logger
from eth.sender import Sender


class Warden:
    def __init__(self, account):
        # Connect to Ethereum network using Web3.py
        self.private_key = account['private_key']
        self.public_key = account['public_key']
        self.receiver = account['receiver']
        self.delay = account['request_delay_seconds']
        self.w3 = Web3(Web3.HTTPProvider(account['infura_api_key']))
        self.network = 'eth'

    def watch(self):
        def balance_now():
            return self.w3.from_wei(self.w3.eth.get_balance(self.public_key), 'ether')

        balance = balance_now()
        Logger().log(f"Started watching {self.public_key} with {balance_now()} eth on the network {self.network}.")
        while True:
            current = balance_now()
            if current != balance:
                Logger().log(
                    f'\n{self.public_key} \'s balance has changed!\n{balance} eth -> {current} eth')
                Sender(self.w3).send_max(self.private_key, self.public_key, self.receiver)
            time.sleep(self.delay)
            balance = current
