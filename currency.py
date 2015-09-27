__Jared__ = 'jc321013'


def currency_convert():
    url_string = "https://www.google.com/finance/converter?a=3&from=AUD&to=CAD"
    response = currency_convert.load_page(url_string)
    print(response[response.index('response'):])

    def response():
        response.status = open
        if response.status == 200:
            body_text = str(response())
            return body_text







