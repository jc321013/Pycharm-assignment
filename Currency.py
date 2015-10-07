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


currency_details_file = open("currency_details.csv")
currency_details_data = currency_details_file.readlines()
print(currency_details_data)
countries = currency_details_data[0].strip().split(",")
currency_details_values = []
for currency_details_line in currency_details_data[5:]:
    currency_details_strings = currency_details_line.strip().split(",")
    currency_details_letter = [str(name) for name in currency_details_strings]
    currency_details_values.append(currency_details_letter)

currency_details_file.close()

for i in range(len(countries)):
    print(countries[i], "currency_details:")
    for currency_details in currency_details_values[i]:
        print(currency_details)
    print(max(currency_details_values[i]))
    print()

currency_details_file = open("currency_details.csv")
currency_details_data = currency_details_file.readlines()
print(currency_details_data)
countries = currency_details_data[0].strip().split(",")
currency_details_values = []
for currency_details_line in currency_details_data[57:]:
    currency_details_strings = currency_details_line.strip().split(",")
    currency_details_letter = [str(name) for name in currency_details_strings]
    currency_details_values.append(currency_details_letter)

currency_details_file.close()

for i in range(len(countries)):
    print(countries[i], "currency_details:")
    for currency_details in currency_details_values[i]:
        print(currency_details)
    print(max(currency_details_values[i]))
    print()





