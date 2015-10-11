__Jared__ = 'jc321013'


class TripExceptionableRuntimeError(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(value)
        if self.value == "":
            raise TripExceptionableRuntimeError('start_date belongs before end_date')
    try:
        country_location = country = []

    except NameError as err:
        print(err)


class TripCountry():
    def __init__(self, name, currency_code, currency_symbol, currency_value):
        self.name = name
        self.currency_code = currency_code
        self.currency_symbol = currency_symbol
        self.currency_value = currency_value

    def travel_country_value(self, value):
        value_str = self.currency_symbol + value
        return value_str

    def travel_currency_value(self, currency_symbol, currency_value):
        self.currency_value = int(currency_value)
        if currency_value != int:
            return "invalid value"
        return self.currency_symbol, self.currency_value

    def __str__(self, name, currency_code, currency_symbol):
        country_location_details = name, currency_code, currency_symbol
        return country_location_details


class TripDetails():
    def __init__(self, location):
        self.country_locations = []
        self.country_locations = location

    def add_date(self, name, start_date, end_date):
        name = str(name)
        start_date = str(start_date)
        end_date = str(end_date)
        trip_tuple = name, start_date, end_date
        if start_date > end_date:
            return RuntimeError(Exception)
        else:
            self.country_locations.append(trip_tuple)

    def current_country(self, date_string):
        date_string == 'YYYY/MM/DD'
        for country_location in self.country_locations:
            name = country_location[0]
            start_date = country_location[1]
            end_date = country_location[2]
            if date_string >= start_date:
                return name
            if date_string <= end_date:
                return name
            else:
                return [""]

    def is_empty(self, country_locations):
        try:
            if len(self.country_locations) == 0:
                return True
        except:
            return False and ""

































