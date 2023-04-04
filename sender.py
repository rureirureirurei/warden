from web3 import Web3, HTTPProvider
import config
from logger import Logger


class Sender:
    def __init__(self, w3):
        self.w3 = w3

    def send(self, private_key, public_key, receiver, amount, gas):
        try:
            nonce = self.w3.eth.get_transaction_count(public_key)
            value = self.w3.to_wei(amount, 'ether')

            tx = {
                'nonce': nonce,
                'to': receiver,
                'value': value,
                'gas': 21000,
                'gasPrice': self.w3.to_wei(gas, 'gwei'),
            }

            signed_tx = self.w3.eth.account.sign_transaction(tx, private_key)
            tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
            message = f'Sent {amount} eth from {public_key} to {receiver} with gas {gas}. tx hash: {tx_hash}'
        except Exception as e:
            message = f'Tried to send {amount} eth from {public_key} to {receiver} with gas {gas} but caught exeption: ' + str(e)
        Logger().log(message)

    def send_max(self, private_key, public_key, receiver):
        balance = self.w3.eth.get_balance(public_key)
        gas = self.w3.to_wei('60', 'gwei')  # TODO
        epsilon = 1000
        available = balance - gas - epsilon
        self.send(private_key, public_key, receiver, available, gas)
