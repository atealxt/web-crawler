from bs4 import BeautifulSoup
from com.zhyfoundry.spider import Parser
from com.zhyfoundry.spider.Parser import ParseResult
import traceback

class Parser2(Parser.Parser):

    def __init__(self):
        pass

    def needLogin(self, source):
        try:
            soup = BeautifulSoup(source)
        except:
            print 'Parse html error:'
            print source
            print ''
            print traceback.format_exc()
            return ParseResult(None, None)

        username = soup.find('input', id="username_field")
        if username != None:
            return True
        return False

