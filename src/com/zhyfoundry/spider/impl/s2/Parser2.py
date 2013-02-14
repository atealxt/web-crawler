from com.zhyfoundry.spider.Parser import ParseResult
from com.zhyfoundry.spider.impl import BaseParser
from com.zhyfoundry.spider.impl.CRM import Enterprise
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

    def parse(self, source, url):
        soup = self.getSoup(source)
        if soup is ParseResult:
            return soup

        _name = str(soup.find('div', itemprop="name").string)
        _contact = ''
        _tel = str(soup.find('span', itemprop="telephone").string)
        _mobileNo = ''
        faxNo = soup.find('span', itemprop="faxNumber")
        if faxNo != None:
            _faxNo = str(faxNo.string)
        else:
            _faxNo = ''
        siteURL = soup.find('a', class_="p_SiteInternet")
        if siteURL != None:
            _source = siteURL['href']
            _email = '' #TODO
        else:
            _source = ''
            _email = ''
        _remark = 'Crawl from: ' + url
        _keyword = ' '.join([a.get_text() for a in soup.find_all('span', itemprop="streetAddress")]) #address
        _countryName = self.getCountryCode(str(soup.find('span', itemprop="addressCountry").string))
        enterprise = Enterprise(_name, _contact, _email, _tel, _mobileNo, _faxNo, _source, _remark, _keyword, _countryName)
        return ParseResult(enterprise, [])
