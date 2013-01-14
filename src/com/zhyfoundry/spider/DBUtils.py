from com.zhyfoundry.spider import Configuration
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
                self.dbname = Configuration.Configuration.get('Database', 'dbname');
                self.host = Configuration.Configuration.get('Database', 'host');
                self.username = Configuration.Configuration.get('Database', 'username');
                self.password = Configuration.Configuration.get('Database', 'password');
            return mysql.connector.connect(user=self.username, password=self.password, host=self.host, database=self.dbname)
        except mysql.connector.Error:
            raise

'''
TODO plus:
Connection pool
'''