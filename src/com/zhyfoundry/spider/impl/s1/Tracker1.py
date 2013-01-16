from com.zhyfoundry.spider.impl import BaseTracker

class Tracker1(BaseTracker.BaseTracker):

    def __init__(self):
        pass

    def track(self, seeds, source, basePath, spiderId):
        if seeds != None:
            for e in seeds:
                canonizeURL = self.canonizeURL(basePath + e['href'])
                _id = self.getURLId(canonizeURL)
                if self.isNewSeed(canonizeURL, _id):
                    print 'Find new url: ' + canonizeURL
                    self.saveURL(spiderId, canonizeURL, source)
                else:
                    self.updateTrackTime(_id)
        self.updateTrackTime(source)

    def isNewSeed(self, seed, _id):
        return _id == None
