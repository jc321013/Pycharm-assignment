__Jared__ = 'jc321013'

currency_details_file = open("currency_details.csv")
currency_details_data = currency_details_file.readlines()
print(currency_details_data)
countries = currency_details_data[0].strip().split(",")
currency_details_values = []
for currency_details_line in currency_details_data[5:]:
    currency_details_strings = currency_details_line.strip().split(",")
    currency_details_letter = [str(name) for name in currency_details_strings]
    currency_details_values.append(currency_details_letter)

for i in range(len(countries)):
    print(countries[i], "currency_details:")
    for currency_details in currency_details_values[i]:
        print(currency_details)
    print(max(currency_details_values[i]))
    print()


class Error(Exception):
    def __init__(self, name=""):
        self._countries = 'Australia, AUD,$'
        if name != 'Australia,AUD,$':
            raise NameError('Other countries are not valid')
        self._countries += name

    try:
        countries = currency_details(country='Australia,AUD,$')
        countries.find_country('Australia,AUD,$')
    except NameError as err:
        print(err)

































