# -*- coding: utf-8 -*-

from com.zhyfoundry.spider import Tracker
import unittest
class Test(unittest.TestCase):

    def testCanonizeURL(self):
        c = Tracker.Tracker()

        url1 = c.canonizeURL('http://www.baidu.com/');
        self.assertEqual('http://www.baidu.com:80/', url1)

        url2 = c.canonizeURL('http://www.baidu.com/s?wd=测试&pn=10&ie=utf-8&usm=2&rsv_page=1');
        self.assertEqual('http://www.baidu.com:80/s?wd=%B2%E2%CA%D4&pn=10&ie=utf-8&usm=2&rsv_page=1', url2)

        url3 = c.canonizeURL('http://stackoverflow.com/questions/5834808/designing-a-web-crawler?answertab=votes#tab-top');
        self.assertEqual('http://stackoverflow.com:80/questions/5834808/designing-a-web-crawler?answertab=votes', url3)

        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()