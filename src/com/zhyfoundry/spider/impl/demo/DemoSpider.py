from com.zhyfoundry.spider import Spider, Configuration
from com.zhyfoundry.spider.impl.demo import DemoFetcher, DemoParser, DemoTracker

class DemoSpider(Spider.Spider):

    def __init__(self):
        '''
        Constructor
        '''
    def crawl(self):

        fetcher = DemoFetcher.DemoFetcher();
        config = Configuration.Configuration(60, 1, 600, 2, 1);
        html = fetcher.fetch("http://python.org/", config);
        html = html.decode('gbk').encode('utf-8')

        parser = DemoParser.DemoParser()
        parseResult = parser.parse(html)
        print "http://python.org" + parseResult.content

        tracker = DemoTracker.DemoTracker()
        tracker.track(parseResult.newSeeds, "http://python.org/")
