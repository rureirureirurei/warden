import config
from warden import Warden
from logger import Logger
from sender import Sender
from web3 import Web3#TODO REMOVE

if __name__ == '__main__':
    try:
        Warden().watch()
    except Exception as e:
        message = "Exception during the warden's watch:\n" + str(e)
        Logger().log(message)
