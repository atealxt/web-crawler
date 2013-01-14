from com.zhyfoundry.spider import Configuration
from com.zhyfoundry.spider.impl import BaseSpider
from com.zhyfoundry.spider.impl.s1 import Fetcher1

class Spider1(BaseSpider.BaseSpider):

    def __init__(self):
        super(Spider1, self).__init__()

    def crawl(self):

        urlTracker = self.fetchURL();
        print 'URL to fetch: ' + str(urlTracker)
        fetcher = Fetcher1.Fetcher1();
        html = fetcher.fetch(urlTracker.url, Configuration.Configuration.readFromFile());
        #print 'Fetch result: '
        #print html

