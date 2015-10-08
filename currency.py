__Jared__ = 'jared_000'

import web_utility


def convert(amount, home_currency_code, location_currency_code):
    try:
        amount = float(amount)
        home_currency_code != location_currency_code

        url_string = "https://www.google.com/finance/converter?a={}&from={}&to={}".format(str(amount),
                                                                                          home_currency_code,
                                                                                          location_currency_code)

        outcome = web_utility.load_page(url_string)
        substring = (outcome[outcome.index('result'):])
        section = substring.split('>')
        end_index = (section[2].find(' '))
        currency_converted_amount = float(section[2][0:end_index])
        return currency_converted_amount
    except:
        return -1


print(convert(1, 'AUD', 'JPY'))


def get_details(country_name):
    currency_details_file = open("currency_details.txt", 'r', encoding='utf-8')
    currency_details_data = currency_details_file.readlines()
    try:
        for currency_details_line in currency_details_data:
            currency_details_strings = currency_details_line.strip().split(",")
            if country_name == currency_details_strings[0]:
                return tuple(currency_details_strings)
    except:
        return tuple("")

    currency_details_file.close()

print(get_details('Australia'))

