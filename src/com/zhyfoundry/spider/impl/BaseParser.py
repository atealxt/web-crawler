from bs4 import BeautifulSoup
from com.zhyfoundry.spider import Parser
from com.zhyfoundry.spider.Parser import ParseResult
import traceback

class BaseParser(Parser.Parser):

    DICT_COUNTRY = {'United States': 'US', 'Canada' : 'CA'}; #TODO

    def __init__(self):
        super(BaseParser, self).__init__()

    def getSoup(self, source):
        try:
            return BeautifulSoup(source)
        except:
            print 'Parse html error:'
            print source
            print ''
            print traceback.format_exc()
            return ParseResult(None, None)

    def getCountryCode(self, country):
        try:
            return self.DICT_COUNTRY[country]
        except KeyError:
            self.DICT_COUNTRY[country] = country
            return country
