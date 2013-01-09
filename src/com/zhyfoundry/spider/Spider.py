import ConfigParser
import mysql.connector
import os

class Spider(object):

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
            configParser = ConfigParser.ConfigParser()
            config_fn = os.path.join(os.path.dirname(__file__), '..', '..' , '..', 'spider.cfg')
            configParser.read(config_fn)
            dbname = configParser.get('Database', 'dbname');
            host = configParser.get('Database', 'host');
            username = configParser.get('Database', 'username');
            password = configParser.get('Database', 'password');
            cnx = mysql.connector.connect(user=username, password=password, host=host, database=dbname)
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

    def crawl(self):
        print "Implement by subclass..."

'''
TODO plus:
Distribution design
'''