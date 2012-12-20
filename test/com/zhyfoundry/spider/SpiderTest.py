import unittest
from com.zhyfoundry.spider import Spider

class SpiderTest(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testCrawl(self):
        c = Spider.Spider()
        c.crawl()
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()