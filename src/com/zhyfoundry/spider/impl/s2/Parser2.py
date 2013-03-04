from com.zhyfoundry.spider.Parser import ParseResult
from com.zhyfoundry.spider.impl import BaseParser
from com.zhyfoundry.spider.impl.CRM import Enterprise
from com.zhyfoundry.spider.impl.s2 import Fetcher2
import re
import time

class Parser2(BaseParser.BaseParser):

    def __init__(self):
        super(Parser2, self).__init__()

    def needLogin(self, source):
        soup = self.getSoup(source)
        if isinstance(soup, ParseResult):
            return False

        username = soup.find('input', id="username_field")
        if username != None:
            return True
        return False

    def parseSearchResult(self, source):
        soup = self.getSoup(source)
        if isinstance(soup, ParseResult):
            return soup

        archs = soup.find_all('a', href=re.compile("com/live/"), class_="color_bleu")
        arch = soup.find('a', id="next_page")
        return ParseResult(None, archs, arch)

    def isDetailPage(self, source):
        soup = self.getSoup(source)
        if isinstance(soup, ParseResult):
            return False

        result_research = soup.find('div', class_="company_description")
        if result_research != None:
            return True
        return False

    def parse(self, source, url, config):
        soup = self.getSoup(source)
        if isinstance(soup, ParseResult):
            return soup

        _name = str(soup.find('div', itemprop="name").string)
        _contact = '' # TODO find contact under `Executives`
        tel = soup.find('span', itemprop="telephone")
        if tel != None:
            _tel = str(tel.string)
        else:
            _tel = ''
        _mobileNo = ''
        faxNo = soup.find('span', itemprop="faxNumber")
        if faxNo != None:
            _faxNo = str(faxNo.string)
        else:
            _faxNo = ''
        _source = None
        siteURL = soup.find('a', class_="p_SiteInternet")
        if siteURL != None:
            _source = siteURL['href']
        else:
            site = soup.find('strong', text=re.compile("Web Site"))
            if site != None:
                siteURL = site.parent.find_next("td")
                if siteURL != None:
                    _source = siteURL.string.strip()
        if _source != None:
            print 'Try to find email'
            siteHtml = self.fetchSiteHtml(_source, config)
            _email = self.getEmail(siteHtml)
            if _email != '':
                print 'Found email: ' + _email
            else:
                if siteHtml != None:
                    soupSite = self.getSoup(siteHtml)
                    if isinstance(soupSite, ParseResult):
                        pass # do nothing
                    else:
                        for tag in soupSite.find_all('a', href=True):
                            if self.isInnerURL(url, tag['href']) == False:
                                continue
                            fullUrl = self.getFullUrl(_source, tag['href']);
                            pageHtml = self.fetchSiteHtml(fullUrl, config)
                            _email = self.getEmail(pageHtml)
                            if _email != '':
                                print 'Found email: ' + _email
                                break
        else:
            _source = ''
            _email = ''
        _remark = 'Crawl from: ' + url
        _keyword = ' '.join([a.get_text() for a in soup.find_all('span', itemprop="streetAddress")]) #address
        _countryName = str(soup.find('span', itemprop="addressCountry").string)
        enterprise = Enterprise(_name, _contact, _email, _tel, _mobileNo, _faxNo, _source, _remark, _keyword, _countryName)
        return ParseResult(enterprise, [])

    def isInnerURL(self, url, href):
        if href.startswith('/'):
            return True
        _idxDot = href.find(".", 11) # before the second dot
        if url.startswith(href[:_idxDot]):
            return True
        return False

    def getFullUrl(self, source, href):
        if href.startswith('http'):
            return href
        _href = href
        if _href.startswith('/') == False:
            _href = "/" + _href;
        _idxSlash = source.find("/", 8)
        if _idxSlash == -1:
            return source + _href;
        else:
            return source[:_idxSlash] + _href;

    def fetchSiteHtml(self, url, config):
        print 'Find email from page: ' + url
        fetcher = Fetcher2.Fetcher2()
        html = fetcher.fetch(url, config)
        print 'Sleep ' + str(config.interval) + ' second.'
        time.sleep(config.interval)
        return html

#    regexp_email = r'''(\w+[.|\w])*@(\w+[.])*\w+'''
    regexp_email = r'''([\w\-\.+]+@\w[\w\-]+\.+[\w\-]+)'''
    pattern = re.compile(regexp_email)
    def getEmail(self, html):
        if html == None:
            return ''
        emailAddresses = set(re.findall(self.pattern, html))
        return ';'.join(emailAddresses)
