from com.zhyfoundry.spider import Fetcher, Configuration
import cookielib
import mechanize
import socket

class BaseFetcher(Fetcher.Fetcher):

    browser = None
    userAgent = Configuration.Configuration.get('Spider', 'userAgent')

    def __init__(self):
        if not self.browser:
            self.browser = self.initBrowser(self.__module__)

    @classmethod
    def initBrowser(self, _code):

        br = mechanize.Browser()

        # Cookie Jar
        cj = cookielib.LWPCookieJar()
        br.set_cookiejar(cj)

        # Browser options
        br.set_handle_equiv(True)
        #br.set_handle_gzip(True)
        br.set_handle_redirect(True)
        br.set_handle_referer(True)
        br.set_handle_robots(False)

        # Follows refresh 0 but not hangs on refresh > 0
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

        # Want debugging messages?
        #br.set_debug_http(True)
        #br.set_debug_redirects(True)
        #br.set_debug_responses(True)

        # TODO configurable
        br.addheaders = [('User-agent', self.userAgent)]

        return br

    def fetch(self, url, config):
        try:
            r = self.browser.open(url, timeout = config.connectTimeout)
        except mechanize.URLError, exc:
            if isinstance(exc.reason, socket.timeout):
                print "Timeout occurred"
                return None
            raise
        html = r.read()
        return html
