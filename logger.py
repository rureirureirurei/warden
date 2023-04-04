from datetime import datetime


class Logger:
    def __init__(self, logfile_path='logs'):
        self.path = logfile_path
        pass

    def log(self, message):
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        with open(self.path, 'a') as f:
            f.write(time + ": " + message + '\n\n')
