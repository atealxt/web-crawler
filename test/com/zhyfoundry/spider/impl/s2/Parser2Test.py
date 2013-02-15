from com.zhyfoundry.spider import Configuration
from com.zhyfoundry.spider.impl.s2 import Parser2
import unittest

class Parser2Test(unittest.TestCase):

    def testParse(self):
        c = Parser2.Parser2()

        config = Configuration.Configuration.readFromFile();
        emails = c.getEmail('http://www.zhyfoundry.com/contact/', config);
        self.assertTrue(emails != '')
        print emails

        emails = c.getEmail('http://www.baidu.com', config);
        self.assertEqual('', emails)

        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()