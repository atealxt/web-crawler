from com.zhyfoundry.spider import Spider, DBUtils
import mysql.connector

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