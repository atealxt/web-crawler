from com.zhyfoundry.spider.impl.demo import DemoSpider
import unittest

class DemoSpiderTest(unittest.TestCase):

    def testCrawl(self):
        c = DemoSpider.DemoSpider()
        c.crawl()
        pass

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
