from com.zhyfoundry.spider.impl.s1 import Spider1
import unittest

class Spider1Test(unittest.TestCase):

    def testCrawl(self):
        c = Spider1.Spider1()
        c.crawl('2013-01-16 17:46:41')
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()