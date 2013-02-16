from com.zhyfoundry.spider import Configuration
from com.zhyfoundry.spider.impl import BaseSpider
from com.zhyfoundry.spider.impl.CRM import CRM
from com.zhyfoundry.spider.impl.s1 import Fetcher1, Parser1, Tracker1
import time
import traceback

class Spider1(BaseSpider.BaseSpider):

    def __init__(self):
        super(Spider1, self).__init__()

    def crawl(self, trackingTimestamp):

        config = Configuration.Configuration.readFromFile();
        countLimit = 65535 if config.maxFetchCount == -1 else config.maxFetchCount
        urlsToFetch = self.fetchURL(trackingTimestamp, countLimit)
        if len(urlsToFetch) == 0:
            print 'No URL to fetch.'
            return
        for url in urlsToFetch:
            print 'URL to fetch: ' + str(url)
            fetcher = Fetcher1.Fetcher1()
            html = fetcher.fetch(url.url, config)

            parser = Parser1.Parser1()
            parseResult = parser.parse(html, url.url)

            if parseResult.content != None:
                try:
                    CRM.saveEnterprise(parseResult.content);
                except:
                    print traceback.format_exc()

            tracker = Tracker1.Tracker1()
            basePath = url.url[:url.url.find("/", 7)]
            tracker.updateTrackTime(url.id)
            tracker.track(parseResult.newSeeds, url.id, self.id, basePath)

            print 'Sleep ' + str(config.interval) + ' second.'
            time.sleep(config.interval)

'''
TODO plus:
maxExecuteTime
numOfParallel
'''