import requests

url1 = 'https://api.ipify.org?format=json'
url2 = 'https://api.myip.com'
url3 = 'https://httpbin.org/ip'
url4 = 'https://ip.seeip.org/jsonip?'
url5 = 'https://jsonip.com/'
url6 = 'http://ip-api.com/json/'



def show(text, url=""):
    print('*' * 80)
    print(url)
    print(text)
    print('*' * 80)

r1 = requests.get(url6)
show(r1.json())

r1 = requests.get(url5)
show(r1.json())

r1 = requests.get(url3)
show(r1.json())



