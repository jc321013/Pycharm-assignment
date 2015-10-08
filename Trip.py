__Jared__ = 'jc321013'


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

































