import requests
from threading import Thread

from loader import Loader
from collector import Collector


url1 = 'https://httpbin.org/ip'
url6 = 'http://ip-api.com/json/'



class ProxyCarousel:
    def __init__(self, *url, thread_target=40, timeout=6):
        self.urls = self.check_args(*url)
        self.OUT = {}
        self.BASE = Loader()
        self.timeout_proxy = timeout
        self.thread_target = thread_target
        self.COL = Collector()

    
    def proxy_template(self, type_proxy):
        if type_proxy == 'http':
            temp = {
                'http' : 'http://',
                'https' : 'http://'
            }

        elif type_proxy == 'https':
            temp = {
                'http' : 'http://',
                'https' : 'https://'
            }
        
        elif type_proxy == 'socks4':
            temp = {
                'http' : "socks4://",
                'https' : "socks4://"
            }
        
        elif type_proxy == 'socks5':
            temp = {
                'http' : "socks5://",
                'https' : "socks5://"
            }

        return temp

    def request_carousel(self, type_proxy):
        for url in self.urls:
            print('Target: ', url)
            self.OUT[url] = []
            
            reqs = []
            num = 0
            for i in range(self.thread_target):
                num += 1
                print('Thread no: ', num)
                proxy = self.random_proxy(type_proxy)
                t = Thread(target=self.simple_request, args=(url, proxy), daemon=True)
                reqs.append(t)
                t.start()
            for t in reqs:
                t.join()
        
        print("OUT: ", self.OUT)
        self.COL.trash_header(self.OUT)



    def random_proxy(self, type_proxy):
        temp = self.proxy_template(type_proxy)
        proxy = self.BASE.random_proxy(type_proxy)
        for v in temp:
            temp[v] += proxy[0]
        return temp
        

    def check_args(self, *args):
        temp = set()
        if not args:
            return None
        else:
            for a in args:
                temp.add(a.rstrip())
        return temp

    def simple_request(self, url, proxy):
        if len(self.OUT[url]) > 0:
            return None
        print('RANDOM PROXY: ', proxy)
        try:
            response = requests.get(url, proxies=proxy, timeout=self.timeout_proxy)
            if response.status_code == 200:
                self.OUT[url].append((response, proxy))
                return response


        except Exception as e:
            # print('Error Connection: ', e)
            return None


        



        
###########
url5 = 'https://jsonip.com/'
url6 = 'http://ip-api.com/json/'
C = ProxyCarousel(url5, url6)
C.request_carousel('socks5')











