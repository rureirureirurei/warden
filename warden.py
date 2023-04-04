from web3 import Web3
import config
import time
from logger import Logger
from sender import Sender


class Warden:
    def __init__(self):
        # Connect to Ethereum network using Web3.py
        self.w3 = Web3(Web3.HTTPProvider(config.INFURA_KEY))

    def watch(self):
        print("The warden is standing guard ...")
        print(f"Sentry keeps his eye on the target..             (from) {config.PUBLIC_KEY}")
        print(f"And will take action to prevent any breach...    ( to ) {config.RECEIVER}")
        # Get the initial balance of the account
        def balance_now():
            return self.w3.from_wei(self.w3.eth.get_balance(config.PUBLIC_KEY), 'ether')

        balance = balance_now()

        while True:
            current = balance_now()
            if current != balance:
                Logger().log(f'Account {config.PUBLIC_KEY} \'s balance has changed! was: {balance}, became: {current}')
                Sender(self.w3).send_max(config.PRIVATE_KEY, config.PUBLIC_KEY, config.RECEIVER)
            time.sleep(config.WATCHER_DELAY)
            balance = current

