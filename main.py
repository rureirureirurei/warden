from warden import Warden
from logger import Logger

if __name__ == '__main__':
    try:
        Warden().watch()
    except Exception as e:
        message = "Exception during the warden's watch:\n" + str(e)
        Logger().log(message)
