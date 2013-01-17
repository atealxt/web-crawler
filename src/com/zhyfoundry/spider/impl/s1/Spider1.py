from com.zhyfoundry.spider import Configuration
from com.zhyfoundry.spider.impl import BaseSpider
from com.zhyfoundry.spider.impl.CRM import CRM
from com.zhyfoundry.spider.impl.s1 import Fetcher1, Parser1, Tracker1
import traceback

class Spider1(BaseSpider.BaseSpider):

    def __init__(self):
        super(Spider1, self).__init__()

    def crawl(self, trackingTimestamp):

        urlTracker = self.fetchURL(trackingTimestamp)
        if urlTracker == None:
            print 'No URL to fetch.'
            return
        print 'URL to fetch: ' + str(urlTracker)
        fetcher = Fetcher1.Fetcher1()
        html = fetcher.fetch(urlTracker.url, Configuration.Configuration.readFromFile())

        parser = Parser1.Parser1()
        parseResult = parser.parse(html, urlTracker.url)

        if parseResult.content != None:
            try:
                CRM.saveEnterprise(parseResult.content);
            except:
                print traceback.format_exc()

        tracker = Tracker1.Tracker1()
        basePath = urlTracker.url[:urlTracker.url.find("/", 7)]
        tracker.track(parseResult.newSeeds, urlTracker.id, basePath, self.id)
