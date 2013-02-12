from com.zhyfoundry.spider import Configuration
from com.zhyfoundry.spider.impl import BaseSpider
from com.zhyfoundry.spider.impl.s2 import Fetcher2, Parser2, Tracker2
import time

class Spider2(BaseSpider.BaseSpider):

    def __init__(self):
        super(Spider2, self).__init__()

    def crawl(self, trackingTimestamp, keyword):

        config = Configuration.Configuration.readFromFile();
        countLimit = 65535 if config.maxFetchCount == -1 else config.maxFetchCount
        urlsToFetch = self.fetchURL(trackingTimestamp, countLimit)
        if len(urlsToFetch) == 0:
            print 'No URL to fetch.'
            return
        fetcher = Fetcher2.Fetcher2()
        parser = Parser2.Parser2()
        count = 0
        for url in urlsToFetch:
            if count >= countLimit:
                print 'Fetch count limitation reached: ' + str(countLimit)
                break;
            count += 1;
            print 'URL to fetch: ' + str(url)
            html = fetcher.fetch(url.url, config)

            if parser.needLogin(html):
                print 'Need to Login'
                html = fetcher.login(self.username, self.password)
                if parser.needLogin(html):
                    raise Exception("Login fail!")
                print 'Login success!'
                html = fetcher.fetch(url.url, config)

            if parser.isDetailPage(html):
                print 'TODO'
            elif keyword != None:
                print 'Search term: ' + keyword
                html = fetcher.search(keyword)
                tracker = Tracker2.Tracker2()
                tracker.updateTrackTime(url.id)
                while (True):
                    parseSearchResult = parser.parseSearchResult(html)
                    tracker.track(parseSearchResult.newSeeds, url.id, self.id, None)
                    if parseSearchResult.newSeedRightNow == None or count >= countLimit:
                        break
                    html = fetcher.fetch(parseSearchResult.newSeedRightNow['href'], config)
                    count += 1;

            print 'Sleep ' + str(config.interval) + ' second.'
            time.sleep(config.interval)

