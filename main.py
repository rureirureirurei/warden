import config
from warden import Warden
from logger import Logger
from sender import Sender
from web3 import Web3#TODO REMOVE

if __name__ == '__main__':
    try:
        w3 = Web3(Web3.HTTPProvider(config.INFURA_KEY))#TODO REMOVE
        Sender(w3).send_max(config.PRIVATE_KEY, config.PUBLIC_KEY, config.RECEIVER)
        #Warden().watch()
    except Exception as e:
        message = "Exception during the warden's watch:\n" + str(e)
        Logger().log(message)
