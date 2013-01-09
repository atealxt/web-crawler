import ConfigParser
import os

class Configuration(object):

    def __init__(self, connectTimeout, maxFetchCount, maxExecuteTime, numOfParallel, interval):
        self.connectTimeout = connectTimeout
        self.maxFetchCount = maxFetchCount
        self.maxExecuteTime = maxExecuteTime
        self.numOfParallel = numOfParallel
        self.interval = interval

    _instanceFromCfgFile = None

    @classmethod
    def readFromFile(self):
        if not self._instanceFromCfgFile:
            configParser = ConfigParser.ConfigParser()
            config_fn = os.path.join(os.path.dirname(__file__), '..', '..' , '..', 'spider.cfg')
            configParser.read(config_fn)
            connectTimeout = configParser.getint('Spider', 'connectTimeout');
            maxFetchCount = configParser.getint('Spider', 'maxFetchCount');
            maxExecuteTime = configParser.getint('Spider', 'maxExecuteTime');
            numOfParallel = configParser.getint('Spider', 'numOfParallel');
            interval = configParser.getint('Spider', 'interval');
            self._instanceFromCfgFile = self(connectTimeout, maxFetchCount, maxExecuteTime, numOfParallel, interval)
        return self._instanceFromCfgFile;
