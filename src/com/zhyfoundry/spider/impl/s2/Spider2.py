from com.zhyfoundry.spider import Configuration
from com.zhyfoundry.spider.impl import BaseSpider
from com.zhyfoundry.spider.impl.s2 import Fetcher2, Parser2
import time

class Spider2(BaseSpider.BaseSpider):

    def __init__(self):
        super(Spider2, self).__init__()

    def crawl(self, trackingTimestamp):

        config = Configuration.Configuration.readFromFile();
        countLimit = 65535 if config.maxFetchCount == -1 else config.maxFetchCount
        urlTrackers = self.fetchURL(trackingTimestamp, countLimit)
        if len(urlTrackers) == 0:
            print 'No URL to fetch.'
            return
        fetcher = Fetcher2.Fetcher2()
        parser = Parser2.Parser2()
        for urlTracker in urlTrackers:
            print 'URL to fetch: ' + str(urlTracker)
            html = fetcher.fetch(urlTracker.url, config)

            if parser.needLogin(html):
                print 'Need to Login'
                html = fetcher.login(self.username, self.password)
                if parser.needLogin(html):
                    raise Exception("Login fail!")
                print 'Login success!'
                print html

            print 'Sleep ' + str(config.interval) + ' second.'
            time.sleep(config.interval)

