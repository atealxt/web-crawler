from com.zhyfoundry.spider import Configuration
import mysql.connector

class DBUtils(object):

    dbname = Configuration.Configuration.get('Database', 'dbname');
    host = Configuration.Configuration.get('Database', 'host');
    username = Configuration.Configuration.get('Database', 'username');
    password = Configuration.Configuration.get('Database', 'password');

    dbname_crm = Configuration.Configuration.get('Database_CRM', 'dbname');
    host_crm = Configuration.Configuration.get('Database_CRM', 'host');
    username_crm = Configuration.Configuration.get('Database_CRM', 'username');
    password_crm = Configuration.Configuration.get('Database_CRM', 'password');

    def __init__(self):
        pass

    @classmethod
    def getConnection(self):
        try:
            return mysql.connector.connect(user=self.username, password=self.password, host=self.host, database=self.dbname)
        except mysql.connector.Error:
            raise

    @classmethod
    def getConnectionCRM(self):
        try:
            return mysql.connector.connect(user=self.username_crm, password=self.password_crm, host=self.host_crm, database=self.dbname_crm)
        except mysql.connector.Error:
            raise


'''
TODO plus:
Connection pool
'''