# -*- coding: utf-8 -*-

from com.zhyfoundry.spider.impl import BaseTracker
import unittest

class BaseTrackerTest(unittest.TestCase):

    def testCanonizeURL(self):
        c = BaseTracker.BaseTracker()

        self.assertEqual('http://baidu.com:80', c.canonizeURL('baidu.com'))
        self.assertEqual('http://www.baidu.com:80/', c.canonizeURL('www.baidu.com/'))
        self.assertEqual('http://www.baidu.com:80/', c.canonizeURL('http://www.baidu.com/'))
        self.assertEqual('http://www.baidu.com:80', c.canonizeURL('http://www.baidu.com'))
        self.assertEqual('http://www.baidu.com:80', c.canonizeURL('http://www.baidu.com:80'))
        self.assertEqual('https://github.com:443/', c.canonizeURL('https://github.com/'))

        self.assertEqual('http://stackoverflow.com:80/questions/5834808/designing-a-web-crawler?answertab=votes'
                         , c.canonizeURL('http://stackoverflow.com/questions/5834808/designing-a-web-crawler?answertab=votes#tab-top'))

        pass

    def testExistURL(self):
        c = BaseTracker.BaseTracker()
        self.assertEqual(False, c.existURL('asddsa.com'))
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()