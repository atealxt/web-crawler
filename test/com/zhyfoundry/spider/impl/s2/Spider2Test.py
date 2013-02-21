from com.zhyfoundry.spider.impl.s2 import Spider2
import unittest

class Spider2Test(unittest.TestCase):

    def testCrawl(self):
        c = Spider2.Spider2()
        c.crawl('2014-01-17 22:06:06', 'valve')
#        c.crawl('2014-01-17 22:06:06')
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()