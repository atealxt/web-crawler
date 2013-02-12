from com.zhyfoundry.spider.Parser import ParseResult
from com.zhyfoundry.spider.impl import BaseParser
import re

class Parser2(BaseParser.BaseParser):

    def __init__(self):
        super(Parser2, self).__init__()

    def needLogin(self, source):
        soup = self.getSoup(source)
        if soup is ParseResult:
            return soup

        username = soup.find('input', id="username_field")
        if username != None:
            return True
        return False

    def parseSearchResult(self, source):
        soup = self.getSoup(source)
        if soup is ParseResult:
            return soup

        archs = soup.find_all('a', href=re.compile("com/live/"), class_="color_bleu")
        arch = soup.find('a', id="next_page")
        return ParseResult(None, archs, arch)

    def isDetailPage(self, source):
        soup = self.getSoup(source)
        if soup is ParseResult:
            return soup

        result_research = soup.find('div', class_="company_description")
        if result_research != None:
            return True
        return False
