class Parser(object):

    def __init__(self):
        '''
        Constructor
        '''

    def parse(self, source):
        print "Implement by subclass..."

    # TODO Method to remove html tag

class ParseResult(object):

    def __init__(self, content, newSeeds, newSeedRightNow = None):
        self.content = content
        self.newSeeds = newSeeds
        self.newSeedRightNow = newSeedRightNow
