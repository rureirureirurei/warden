from eth.warden import Warden as ethWarden
from arbitrum.warden import Warden as arbitrumWarden

from logger import Logger
from config import accounts

import multiprocess as mp

if __name__ == '__main__':
    watchers = []
    for account in accounts:
        network = account['network']

        if network == 'eth':
            pass
        #   watcher = ethWarden(account, config['infura_api_key'])
        elif network == 'arbitrum':
            watcher = arbitrumWarden(account)
        else:
            raise Exception(f"{account['network']} is not supported")

        def start(w):
            try:
                w.watch()
            except Exception as e:
                message = "Exception:\n" + str(e)
                Logger().log(message)

        p = mp.Process(target=start, args=(watcher,))
        p.start()
        watchers.append(p)

