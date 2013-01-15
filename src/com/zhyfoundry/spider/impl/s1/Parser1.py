from bs4 import BeautifulSoup
from com.zhyfoundry.spider import Parser
from com.zhyfoundry.spider.Parser import ParseResult
from com.zhyfoundry.spider.impl.CRM import Enterprise
import re

class Parser1(Parser.Parser):

    def __init__(self):
        pass

    def parse(self, source):
        soup = BeautifulSoup(source)

        archs = soup.findAll(href = re.compile("action=profile&cid="))

        if len(archs) > 0:
            return ParseResult(None, archs)

        tr = soup.select(".bodycopy > tbody > tr")
        if len(tr) == 9:
            _name = tr[0].find_all("td")[1].string
            _contact = ''
            _email = tr[7].select("td > a")[0].string
            _tel = tr[5].find_all("td")[1].string
            _mobileNo = ''
            _faxNo = tr[6].find_all("td")[1].string
            _source = tr[8].find_all("td")[1].string
            _remark = 'Crawl from: ' + source
            _keyword = ' '.join(tr[1].find_all("td")[1].strings) #address
            _countryName = 'UK'
            enterprise = Enterprise(_name, _contact, _email, _tel, _mobileNo, _faxNo, _source, _remark, _keyword, _countryName)
            return ParseResult(enterprise, [])


