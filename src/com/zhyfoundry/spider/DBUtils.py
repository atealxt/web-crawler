import ConfigParser
import mysql.connector
import os

class DBUtils(object):

    dbname = None
    host = None
    username = None
    password = None

    def __init__(self):
        pass

    @classmethod
    def getConnection(self):
        try:
            if not self.dbname:
                configParser = ConfigParser.ConfigParser()
                config_fn = os.path.join(os.path.dirname(__file__), '..', '..' , '..', 'spider.cfg')
                configParser.read(config_fn)
                self.dbname = configParser.get('Database', 'dbname');
                self.host = configParser.get('Database', 'host');
                self.username = configParser.get('Database', 'username');
                self.password = configParser.get('Database', 'password');
            return mysql.connector.connect(user=self.username, password=self.password, host=self.host, database=self.dbname)
        except mysql.connector.Error:
            raise

'''
TODO plus:
Connection pool
'''