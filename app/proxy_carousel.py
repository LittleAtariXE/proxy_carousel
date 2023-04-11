import requests
from threading import Thread

from loader import Loader


# proxy = Loader().random_proxy('http')
# print(proxy)


# proxies = {
#    'http': f'http://{proxy[0]}',
#    'https': f'http://{proxy[0]}',
# }

url1 = 'https://httpbin.org/ip'
url6 = 'http://ip-api.com/json/'
# response1 = requests.get(url1, proxies=proxies, timeout=4)

# print('httpbin.org: ', response1.text)


class ProxyCarousel:
    def __init__(self, *url, thread_target=30):
        self.urls = self.check_args(*url)
        self.OUT = []
        self.BASE = Loader()
        self.timeout_proxy = 6
        self.thread_target = thread_target

    
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
            
            reqs = []
            for i in range(self.thread_target):
                proxy = self.random_proxy(type_proxy)
                t = Thread(target=self.simple_request, args=(url, proxy), daemon=True)
                reqs.append(t)
                t.start()
            for t in reqs:
                t.join()



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
        print('RANDOM PROXY: ', proxy)
        try:
            response = requests.get(url, proxies=proxy, timeout=self.timeout_proxy)
            if response.status_code == 200:
                self.OUT.append(response)
                return response


        except Exception as e:
            print('Error Connection: ', e)
            return None


        



        
###########
K = ProxyCarousel(url6)
print(K.urls)
K.request_carousel('http')
print(K.OUT)
for r in K.OUT:
    print(r.json())






