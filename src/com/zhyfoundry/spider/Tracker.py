class Tracker(object):

    def __init__(self):
        '''
        Reference to how to track URL:
        http://stackoverflow.com/questions/5834808/designing-a-web-crawler
        '''

    def track(self, seeds, source):
        print "Implement by subclass..."

    def isNewSeed(self, seed):
        print "Implement by subclass..."

    def canonizeURL(self, url):
        '''
        TODO
        Add default port
        Encode special character
        Remove URL fragments `#`
        etc..
        '''
        return url

'''
TODO plus:
URL length limitation
Pattern detection
'''