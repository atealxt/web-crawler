from com.zhyfoundry.spider import Tracker

class DemoTracker(Tracker.Tracker):

    def __init__(self):
        '''
        Constructor
        '''

    def track(self, seeds, source):
        for e in seeds:
            if self.isNewSeed(e):
                print 'Find new url: ' + e

    def isNewSeed(self, seed):
        return True
