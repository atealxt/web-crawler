from bs4 import BeautifulSoup
from com.zhyfoundry.spider import Parser
from com.zhyfoundry.spider.Parser import ParseResult
import traceback

class BaseParser(Parser.Parser):

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