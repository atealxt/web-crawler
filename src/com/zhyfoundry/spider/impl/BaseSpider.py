from com.zhyfoundry.spider import Spider, DBUtils
import mysql.connector
import time

class BaseSpider(Spider.Spider):

    id = None

    def __init__(self):
        self._initId()

    @classmethod
    def _initId(self):
        if not self.id:
            #_code = self.__module__ + '.' + self.__class__.__name__
            self.id = self._getId(self.__module__)

    @classmethod
    def _getId(self, _code):

        cursor = None
        cnx = None
        try:
            cnx = DBUtils.DBUtils().getConnection();
            cursor = cnx.cursor()
            cursor.execute('SELECT ID FROM SPIDER WHERE CODE = %s', (_code,))
            row = cursor.fetchone()
            if row is not None:
                return row[0]
            raise Exception("Spider not found! Code: " + _code)
        except mysql.connector.Error:
            raise
        finally:
            if cursor:
                cursor.close()
            if cnx:
                cnx.close()

    @classmethod
    def fetchURL(self, trackingTimestamp = time.strftime('%Y-%m-%d %H:%M:%S'), countLimit = 1):
        self._initId()
        cursor = None
        cnx = None
        try:
            cnx = DBUtils.DBUtils().getConnection();
            cursor = cnx.cursor()
            cursor.execute('SELECT ID, URL FROM URL_TRACKER WHERE SPIDER_ID = %s AND LATEST_TRACK_TIME < %s ORDER BY LATEST_TRACK_TIME DESC LIMIT %s',\
                           (self.id, trackingTimestamp, countLimit))
            row = cursor.fetchone()
            if row is not None:
                return URLTracker(row[0], row[1])
            return None;
        except mysql.connector.Error:
            raise
        finally:
            if cursor:
                cursor.close()
            if cnx:
                cnx.close()

class URLTracker(object):

    def __init__(self, ID, URL):
        self.ID = ID
        self.URL = URL

    def __repr__(self):
        return self.__module__ + '.' + self.__class__.__name__ + '\n ID = ' + str(self.ID) + ', URL = ' + self.URL
