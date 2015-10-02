__Jared__ = 'jared_000'

import urllib.request

x = urllib.request.urlopen("https://www.google.com/finance/converter?a=1&from=AUD&to=JPY")

print(x.read())







