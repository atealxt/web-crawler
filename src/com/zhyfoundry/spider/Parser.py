class Parser(object):

    def __init__(self):
        '''
        Constructor
        '''

    def parse(self, source):
        print "Implement by subclass..."

class ParseResult(object):

    def __init__(self, content, newSeeds):
        self.content = content
        self.newSeeds = newSeeds
