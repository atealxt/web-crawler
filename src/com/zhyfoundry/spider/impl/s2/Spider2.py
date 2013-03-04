from com.zhyfoundry.spider import Configuration
from com.zhyfoundry.spider.impl import BaseSpider
from com.zhyfoundry.spider.impl.CRM import CRM
from com.zhyfoundry.spider.impl.s2 import Fetcher2, Parser2, Tracker2
import time
import traceback

class Spider2(BaseSpider.BaseSpider):

    def __init__(self):
        super(Spider2, self).__init__()

    def crawl(self, trackingTimestamp, keyword = None):

        config = Configuration.Configuration.readFromFile();
        countLimit = 65535 if config.maxFetchCount == -1 else config.maxFetchCount
        urlsToFetch = self.fetchURL(trackingTimestamp, countLimit)
        if len(urlsToFetch) == 0:
            print 'No URL to fetch.'
            return
        fetcher = Fetcher2.Fetcher2()
        parser = Parser2.Parser2()
        count = 0
        tracker = Tracker2.Tracker2()
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
                parseResult = parser.parse(html, url.url, config)
                if parseResult.content != None:
                    try:
                        CRM.saveEnterprise(parseResult.content);
                    except:
                        print traceback.format_exc()
                    tracker.updateTrackTime(url.id)
                    tracker.track(parseResult.newSeeds, url.id, self.id, None)
            elif keyword != None:
                print 'Search term: ' + keyword
                html = fetcher.search(keyword)
                tracker.updateTrackTime(url.id)
                page = 1
                while (True):
                    parseSearchResult = parser.parseSearchResult(html)
                    tracker.track(parseSearchResult.newSeeds, url.id, self.id, None)
                    if parseSearchResult.newSeedRightNow == None or count >= countLimit:
                        print 'parseSearchResult.newSeedRightNow == None: ' + str(parseSearchResult.newSeedRightNow == None)
                        print 'count >= countLimit: ' + str(count >= countLimit)
                        break
                    page += 1
                    print 'Will crawl page ' +  str(page) + ': ' + parseSearchResult.newSeedRightNow['href']
                    print 'Sleep ' + str(config.interval) + ' second.'
                    time.sleep(config.interval)
                    html = fetcher.fetch(parseSearchResult.newSeedRightNow['href'], config)
                    if html == None:
                        retryTimes = 0
                        while (retryTimes < config.maxRetryTimes and html == None):
                            retryTimes += 1
                            print 'Retry ' + str(retryTimes)
                            html = fetcher.fetch(parseSearchResult.newSeedRightNow['href'], config)
                    count += 1

            print 'Sleep ' + str(config.interval) + ' second.'
            time.sleep(config.interval)

