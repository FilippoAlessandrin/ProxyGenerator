from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random
# this function create a list of random proxies that you can use
def createProxyList():
    ua = UserAgent()  # generate a random user agent
    proxies = []  # Will contain proxies [ip, port]
    proxies_req = Request('https://www.sslproxies.org/') # this request retrieves a list of proxies from the site
    proxies_req.add_header('User-Agent', ua.random) # adds the user agent to the header request
    proxies_doc = urlopen(proxies_req).read().decode('utf8') 

    soup = BeautifulSoup(proxies_doc, 'html.parser') 
    proxies_table = soup.find(id='proxylisttable') 

    # Save proxies in the array
    for row in proxies_table.tbody.find_all('tr'):
        proxies.append(row.find_all('td')[0].string+":"+row.find_all('td')[1].string)
    return proxies
 
# this function generates a random integer that is usable as an index for the proxy list
def random_proxy(proxies):
  return random.randint(0, len(proxies) - 1)