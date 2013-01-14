import unittest
from com.zhyfoundry.spider.impl.CRM import CRM

class CRMTest(unittest.TestCase):

    def testGetCountryId(self):
        country_id = CRM.getCountryId('China');
        print 'Country Id: ' + str(country_id)
        self.assertTrue(country_id > 0);
        pass

    def testSaveEnterprise(self):
        CRM.saveEnterprise('testSaveEnterprise', 'admin', 'admin@admin.com', '123456', '234567', '345678', 'zhyfoundry-spider', 'remark', 'keyword', 'China');
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()