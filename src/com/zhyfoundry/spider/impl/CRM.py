from com.zhyfoundry.spider import DBUtils
import mysql.connector

class CRM(object):

    def __init__(self):
        pass

    @classmethod
    def saveEnterprise(self, name = None, contact = '', email = '', tel = '', mobileNo = '', faxNo = '', source = None, remark = '', keyword = '', countryName = None):

        if name is None:
            raise Exception("Enterprise's name can't be null!")
        country_id = self.getCountryId(countryName);
        cursor = None
        cnx = None
        try:
            cnx = DBUtils.DBUtils().getConnectionCRM();
            cursor = cnx.cursor()
            cursor.execute('INSERT INTO ENTERPRISE (`NAME`, `CONTACT`, `EMAIL`, `TEL`, `MOBILE_NO`, `FAX_NO`, `SOURCE`, `REMARK`, `KEYWORD`, `COUNTRY_ID`, `STATUS`, `COUNT_MAIL_SENT`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',\
                           (name, contact, email, tel, mobileNo, faxNo, source, remark, keyword, country_id, 0, 0))
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

    @classmethod
    def getCountryId(self, countryName):
        # TODO cache
        cursor = None
        cnx = None
        try:
            cnx = DBUtils.DBUtils().getConnectionCRM();
            cursor = cnx.cursor()
            cursor.execute('SELECT ID FROM COUNTRY WHERE NAME = %s', (countryName, ))
            row = cursor.fetchone()
            if row is not None:
                return row[0]
            raise Exception("Country not exist: " + countryName)
        except mysql.connector.Error:
            raise
        finally:
            if cursor:
                cursor.close()
            if cnx:
                cnx.close()
