from com.zhyfoundry.spider import Tracker, DBUtils
import mysql.connector

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

    def saveURL(self, spiderId, url, urlSource):

        cursor = None
        cnx = None
        try:
            cnx = DBUtils.DBUtils().getConnection();
            cursor = cnx.cursor()
            cursor.execute('INSERT INTO URL_TRACKER (`SPIDER_ID`, `URL`, `URL_SOURCE`) VALUES (%s, %s, %s)',\
                           (spiderId, url, urlSource))
            cnx.commit()
        except mysql.connector.Error:
            try:
                cnx.rollback()
            except:
                raise
            raise
        finally:
            if cursor:
                cursor.close()
            if cnx:
                cnx.close()

    def getURLId(self, url):
        cursor = None
        cnx = None
        try:
            cnx = DBUtils.DBUtils().getConnection();
            cursor = cnx.cursor()
            cursor.execute('SELECT ID FROM URL_TRACKER WHERE URL = %s', (url,))
            row = cursor.fetchone()
            if row is not None:
                return row[0]
            return None;
        except mysql.connector.Error:
            raise
        finally:
            if cursor:
                cursor.close()
            if cnx:
                cnx.close()

    def updateTrackTime(self, urlId):

        cursor = None
        cnx = None
        try:
            cnx = DBUtils.DBUtils().getConnection();
            cursor = cnx.cursor()
            cursor.execute('UPDATE URL_TRACKER SET LATEST_TRACK_TIME = NOW() WHERE ID = %s', (urlId,))
            cnx.commit()
        except mysql.connector.Error:
            try:
                cnx.rollback()
            except:
                raise
            raise
        finally:
            if cursor:
                cursor.close()
            if cnx:
                cnx.close()

'''
TODO plus:
URL length limitation
Pattern detection
'''