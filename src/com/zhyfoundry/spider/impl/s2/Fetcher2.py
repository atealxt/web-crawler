from com.zhyfoundry.spider.impl import BaseFetcher
import mechanize
import socket

class Fetcher2(BaseFetcher.BaseFetcher):

    def __init__(self):
        super(Fetcher2, self).__init__()

    def login(self, username, password):
        try:
#            self.browser.select_form(name='login_form')
            self.browser.select_form(nr=0)
            self.browser.form['login_header_page_kompass{actionForm.login}'] = username
            self.browser.form['login_header_page_kompass{actionForm.password}'] = password
            _browser = self.browser.submit()
            html = _browser.read()
            return html
        except mechanize.URLError, exc:
            if isinstance(exc.reason, socket.timeout):
                print "Timeout occurred"
                return None
            raise

    def search(self, keyword):
        try:
            self.browser.select_form(name='form_research')
            self.browser.form['mktInfo_BasicSearchPortlet_1wlw-select_key:{actionForm.geoSearch}'] = ['MKT_WW',]
            self.browser.form['mktInfo_BasicSearchPortlet_1wlw-select_key:{actionForm.typeSearch}'] = ['CN',]
            self.browser.form['mktInfo_BasicSearchPortlet_1{actionForm.userParameterSearch}'] = keyword
            _browser = self.browser.submit()
            html = _browser.read()
            return html
        except mechanize.URLError, exc:
            if isinstance(exc.reason, socket.timeout):
                print "Timeout occurred"
                return None
            raise

