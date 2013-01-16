from com.zhyfoundry.spider import Tracker

class BaseTracker(Tracker.Tracker):

    def __init__(self):
        '''
        Reference to how to track URL:
        http://stackoverflow.com/questions/5834808/designing-a-web-crawler
        '''

    def canonizeURL(self, url):
        '''
        TODO
        Encode special character
        etc..
        '''
        _url = url;
        _url = self._addPrefix(_url)
        _url = self._addDefaultPort(_url)
        _url = self._removeFragments(_url)
        return _url

    def _addPrefix(self, url):
        _url = url;
        if not _url.startswith('http'):
            _url = 'http://' + _url
        return _url

    def _addDefaultPort(self, url):
        _url = url;
        _idxColon = -1;
        _https = False;
        if _url.startswith('https'):
            _https = True
            _idxColon = _url.find(":", 6)
            _defaultPort = '443'
        else:
            _idxColon = _url.find(":", 5)
            _defaultPort = '80'
        if _idxColon == -1:
            _idxSlash = -1;
            if _https:
                _idxSlash = _url.find("/", 8)
            else:
                _idxSlash = _url.find("/", 7)
            if _idxSlash == -1:
                _idxSlash = len(_url)
            _url = _url[:_idxSlash] + ':' + _defaultPort + _url[_idxSlash:]
        return _url

    def _removeFragments(self, url):
        _idxPoundSign = url.find('#')
        if _idxPoundSign == -1:
            return url;
        return url[:_idxPoundSign]


'''
TODO plus:
URL length limitation
Pattern detection
'''