from bs4 import BeautifulSoup
from com.zhyfoundry.spider import Parser

class DemoParser(Parser.Parser):

    def __init__(self):
        pass

    def parse(self, source):
        soup = BeautifulSoup(source)
        # print soup.prettify()
        logo = soup.find('img', id="logo")

        return Parser.ParseResult(logo['src'], ['http://www.eclipse.org/', 'http://pydev.org/'])
