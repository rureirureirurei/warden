from web3 import Web3, HTTPProvider
import config
from logger import Logger


class Sender:
    def __init__(self, w3):
        self.w3 = w3

    # BOTH VALUE AND GAS IN WEI
    def send(self, private_key, public_key, receiver, value, gas):
        try:
            nonce = self.w3.eth.get_transaction_count(public_key)
            tx = {
                'nonce': nonce,
                'to': receiver,
                'value': value,
                'gas': 21000,
                'gasPrice': gas,
            }

            signed_tx = self.w3.eth.account.sign_transaction(tx, private_key)
            tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
            message = f'Sent {value} wei from {public_key} to {receiver} with gas {gas}. tx hash: {tx_hash}'
        except Exception as e:
            message = f'Tried to send {value} wei from {public_key} to {receiver} with gas {gas} but caught exeption: ' + str(e)
        Logger().log(message)

    def send_max(self, private_key, public_key, receiver):
        balance = self.w3.eth.get_balance(public_key)
        gas = self.w3.to_wei('50', 'gwei')  # TODO make smart
        epsilon = self.w3.to_wei('0.0015', 'ether')
        available = balance - gas - epsilon
        self.send(private_key, public_key, receiver, available, gas)
