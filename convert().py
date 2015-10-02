__Jared__ = 'jared_000'

import urllib.request
import urllib.parse

x = urllib.request.urlopen("https://www.google.com/finance/converter?a=1&from=AUD&to=JPY")

print(x.read())

url = 'https://www.google.com/finance/converter?a=1&from=AUD&to=JPY&meta=ei%3DO3YOVpGGGMaE0gS7jIuQAQ'
values = {'84.5890': 'aud,yen',
          'submit': 'convert'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url,data)
resp = urllib.request.urlopen(req)
respData = resp.read()

print(respData)

x = urllib.request.urlopen("https://www.google.com/finance/converter?a=84.5890&from=JPY&to=AUD")

print(x.read())

url = 'https://www.google.com/finance/converter?a=84.5890&from=JPY&to=AUD&meta=ei%3DB3gOVuHIB8SN0ATx0buoAQ'
values = {'1': 'aud,yen',
          'submit': 'convert'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url,data)
resp = urllib.request.urlopen(req)
respData = resp.read()

print(respData)





