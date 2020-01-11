from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random
# this function create a list of random proxies that you can use
class RotateProxy:
    proxies=[]
    currentProxy=[]
    currentUserAgent=[]
    currentProxyIndex=0
    ua=""
    def __init__(self):
        self.ua = UserAgent()
        self.currentUserAgent = ""
        self.proxies=[]
        self.currentProxy=[]
        self.currentProxyIndex=0


    def random_agent(self):
        self.currentUserAgent = {
            "User-Agent": self.ua.random
        }

    def createProxyList(self):
        proxies_req = Request('https://www.sslproxies.org/') # this request retrieves a list of proxies from the site
        self.random_agent()
        proxies_req.add_header('User-Agent', self.ua.random) # adds the user agent to the header request
        proxies_doc = urlopen(proxies_req).read().decode('utf8')
        soup = BeautifulSoup(proxies_doc, 'html.parser')
        proxies_table = soup.find(id='proxylisttable')

        # Save proxies in the array
        for row in proxies_table.tbody.find_all('tr'):
            self.proxies.append(row.find_all('td')[0].string+":"+row.find_all('td')[1].string)

    def random_proxy(self):
      return random.randint(0, len(self.proxies) - 1)

    def setCurrentProxy(self):
        proxy_index = self.random_proxy()
        self.currentProxyIndex = proxy_index
        self.currentProxy = {"http": self.proxies[self.currentProxyIndex], "https": self.proxies[self.currentProxyIndex]}

    def rotateProxy(self):
        if(len(self.proxies)<=1):
            self.createProxyList()
            print('Proxy list recreated.')
            self.setCurrentProxy
        else:
            del self.proxies[self.currentProxyIndex]
            self.random_agent()
            self.setCurrentProxy()
            print("proxy Renewed")


