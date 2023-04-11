import os
from pathlib import Path
from random import choice

PROXY_DIR = str(Path(__file__).parent.parent) + "/proxy_list/"

HTTP_FILE = 'http'
HTTPS_FILE = 'https'
SOCKS4_FILE = 'socks4'
SOCKS5_FILE = 'socks5'



class Loader:
    def __init__(self):
        self.BASE_DIR = PROXY_DIR
        self.HTTP = set()
        self.HTTPS = set()
        self.SOCKS4 = set()
        self.SOCKS5 = set()
        self.MAP = {
            HTTP_FILE : self.HTTP,
            HTTPS_FILE : self.HTTPS,
            SOCKS4_FILE : self.SOCKS4,
            SOCKS5_FILE : self.SOCKS5
        }

        self.search_dir()

    def load_content(self, file):
        index = None
        with open(self.BASE_DIR + file, 'r') as f:
            for line in f.readlines():
                if line[0] == '$':
                    index = line[1:].strip()
                    continue
                if line[0] == '#' or line == '\n':
                    continue
                if not index:
                    continue

                self.MAP[index].add(line.rstrip())

    def search_dir(self):
        for d in os.listdir(self.BASE_DIR):
            try:
                self.load_content(d)
            except Exception as e:
                print('[LOADER] Error when load file: ', e)
             
    def random_proxy(self, type_proxy):
        proxy = choice(list(self.MAP[type_proxy]))
        ip = proxy[0:proxy.find(':')]
        port = proxy[proxy.find(':') + 1:]
        return (proxy, ip, port)


#######
