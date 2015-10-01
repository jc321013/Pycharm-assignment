__Jared__ = 'jared_000'

import webbrowser

webbrowser.open('https://www.google.com/finance/converter?a=1&from=AUD&to=JPY')


def currency_convert():
    response = webbrowser.open

    if response == "84.2517":
        body_text = str(response)
        return body_text
    elif response == "":
        print("Invalid response")








