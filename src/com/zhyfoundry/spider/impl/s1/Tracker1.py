from com.zhyfoundry.spider.impl import BaseTracker

class Tracker1(BaseTracker.BaseTracker):

    def __init__(self):
        pass

    def track(self, seeds, source, basePath):
        for e in seeds:
            if self.isNewSeed(e):
                print 'Find new url: ' + str(e['href'])

    def isNewSeed(self, seed):
        return True
