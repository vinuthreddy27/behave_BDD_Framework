import logging
import time

class Loggerr():

    def __init__(self,logger,file_level=logging.INFO):
        self.logger=logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        fmt=logging.Formatter('%(asctime)s - %(filename)s:[%(lineno)s]"-[%(levelnam)s])')
        curr_time=  time.strftime("%Y-%m-%d")
        self.Logfilename= '.\\Logs\\log' + curr_time + '.txt'
        fh=logging.FileHandler(self.Logfilename, mode="w")
        fh.setFormatter(fmt)
        fh.setLevel(file_level)
        self.logger.addHandler(fh)


