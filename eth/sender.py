from web3 import Web3, HTTPProvider
from logger import Logger


class Sender:
    def __init__(self, w3):
        self.w3 = w3

    # BOTH VALUE AND GAS IN WEI
    def send(self, private_key, public_key, receiver, value, gas, intrinsic=21000):
        try:
            nonce = self.w3.eth.get_transaction_count(public_key)
            tx = {
                'nonce': nonce,
                'to': receiver,
                'value': value,
                'gas': intrinsic,
                'gasPrice': gas,
            }

            signed_tx = self.w3.eth.account.sign_transaction(tx, private_key)
            tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
            message = f'\nSent {value} wei\nfrom {public_key} to {receiver}\nwith gas {gas}\ntx hash: {tx_hash}'
        except Exception as e:
            message = f'\nTried to send {value} wei\nfrom {public_key} to {receiver}\nwith gas {gas}\nbut caught exeption:\n' + str(e)
        Logger().log(message)

    def send_max(self, private_key, public_key, receiver):
        balance = self.w3.eth.get_balance(public_key)

        gas = self.w3.to_wei('110000000', 'wei')
        intrinsic = self.w3.to_wei('800000', 'wei')
        epsilon = self.w3.to_wei('90000', 'gwei')
        available = balance - gas - epsilon

        self.send(private_key, public_key, receiver, available, gas, intrinsic)
