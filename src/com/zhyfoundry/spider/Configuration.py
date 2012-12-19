class Configuration(object):

    def __init__(self, connectTimeout, maxFetchCount, maxExecuteTime, numOfParallel, interval):
        self.connectTimeout = connectTimeout
        self.maxFetchCount = maxFetchCount
        self.maxExecuteTime = maxExecuteTime
        self.numOfParallel = numOfParallel
        self.interval = interval
