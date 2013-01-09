import ConfigParser
import mysql.connector
import os

class DBUtils(object):

    def __init__(self):
        pass

    def getConnection(self):
        try:
            configParser = ConfigParser.ConfigParser()
            config_fn = os.path.join(os.path.dirname(__file__), '..', '..' , '..', 'spider.cfg')
            configParser.read(config_fn)
            dbname = configParser.get('Database', 'dbname');
            host = configParser.get('Database', 'host');
            username = configParser.get('Database', 'username');
            password = configParser.get('Database', 'password');
            return mysql.connector.connect(user=username, password=password, host=host, database=dbname)
        except mysql.connector.Error:
            raise

