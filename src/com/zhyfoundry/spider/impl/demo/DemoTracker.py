from com.zhyfoundry.spider.impl import BaseTracker

class DemoTracker(BaseTracker.BaseTracker):

    def __init__(self):
        super(DemoTracker, self).__init__()

    def track(self, seeds, source):
        for e in seeds:
            if self.isNewSeed(e):
                print 'Find new url: ' + e

    def isNewSeed(self, seed):
        return True
