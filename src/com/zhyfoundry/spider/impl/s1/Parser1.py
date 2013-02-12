from bs4 import BeautifulSoup
from com.zhyfoundry.spider import Parser
from com.zhyfoundry.spider.Parser import ParseResult
from com.zhyfoundry.spider.impl.CRM import Enterprise
import re
import traceback

class Parser1(Parser.Parser):

    def __init__(self):
        pass

    def parse(self, source, url):
        try:
            soup = BeautifulSoup(source)
        except:
            print 'Parse html error:'
            print source
            print ''
            print traceback.format_exc()
            return ParseResult(None, None)

        archs = soup.find_all('a', href = re.compile("action=profile&cid="))

        if len(archs) > 0:
            return ParseResult(None, archs)

        tr = soup.select("table.bodycopy > tbody > tr > td table")[0].select("tr")
        if len(tr) == 9:
            _name = str(tr[0].find_all("td")[1].string)
            _contact = ''
            _email = str(tr[7].select("td > a")[0].string)
            _tel = str(tr[5].find_all("td")[1].string)
            _mobileNo = ''
            _faxNo = str(tr[6].find_all("td")[1].string)
            _source = str(tr[8].find_all("td")[1].string)
            _remark = 'Crawl from: ' + url
            _keyword = ' '.join(tr[1].find_all("td")[1].strings) #address
            _countryName = 'UK'
            enterprise = Enterprise(_name, _contact, _email, _tel, _mobileNo, _faxNo, _source, _remark, _keyword, _countryName)
            return ParseResult(enterprise, [])
        return ParseResult(None, None)

