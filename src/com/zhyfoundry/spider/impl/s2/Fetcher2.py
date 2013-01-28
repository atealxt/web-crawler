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
            self.browser = self.browser.submit()
            html = self.browser.read()
            return html
        except mechanize.URLError, exc:
            if isinstance(exc.reason, socket.timeout):
                print "Timeout occurred"
                return None
            raise
