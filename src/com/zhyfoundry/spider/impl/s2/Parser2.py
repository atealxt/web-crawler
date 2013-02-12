from bs4 import BeautifulSoup
from com.zhyfoundry.spider import Parser
from com.zhyfoundry.spider.Parser import ParseResult
import re
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

    def isSearchResultPage(self, source):
        try:
            soup = BeautifulSoup(source)
        except:
            print 'Parse html error:'
            print source
            print ''
            print traceback.format_exc()
            return ParseResult(None, None)

        result_research = soup.find('form', id="result_research")
        if result_research != None:
            return True
        return False

    def parseSearchResult(self, source):
        try:
            soup = BeautifulSoup(source)
        except:
            print 'Parse html error:'
            print source
            print ''
            print traceback.format_exc()
            return ParseResult(None, None)

        archs = soup.find_all('a', href=re.compile("com/live/"), class_="color_bleu")
        arch = soup.find('a', id="next_page") # TODO fetch error when query directly in another session?
        if arch != None:
            archs.append(arch)
        return ParseResult(None, archs)
