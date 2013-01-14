import ConfigParser
import os

class Configuration(object):

    _configParser = ConfigParser.ConfigParser()
    _configParser.read(os.path.join(os.path.dirname(__file__), '..', '..' , '..', 'spider.cfg'))
    _instanceFromCfgFile = None

    def __init__(self, connectTimeout, maxFetchCount, maxExecuteTime, numOfParallel, interval):
        self.connectTimeout = connectTimeout
        self.maxFetchCount = maxFetchCount
        self.maxExecuteTime = maxExecuteTime
        self.numOfParallel = numOfParallel
        self.interval = interval

    @classmethod
    def readFromFile(self):
        if not self._instanceFromCfgFile:
            connectTimeout = self.getint('Spider', 'connectTimeout');
            maxFetchCount = self.getint('Spider', 'maxFetchCount');
            maxExecuteTime = self.getint('Spider', 'maxExecuteTime');
            numOfParallel = self.getint('Spider', 'numOfParallel');
            interval = self.getint('Spider', 'interval');
            self._instanceFromCfgFile = self(connectTimeout, maxFetchCount, maxExecuteTime, numOfParallel, interval)
        return self._instanceFromCfgFile;

    def __repr__(self):
        return self.__module__ + '.' + self.__class__.__name__ + '\n connectTimeout = ' + str(self.connectTimeout)\
             + ', maxFetchCount = ' + str(self.maxFetchCount)\
             + ', maxExecuteTime = ' + str(self.maxExecuteTime)\
             + ', numOfParallel = ' + str(self.numOfParallel)\
             + ', interval = ' + str(self.interval)\

    @classmethod
    def get(self, section, key):
        return self._configParser.get(section, key);

    @classmethod
    def getint(self, section, key):
        return self._configParser.getint(section, key);
