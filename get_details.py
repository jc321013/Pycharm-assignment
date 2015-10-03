__jared__ = 'jc321013'

currency_details_file = open("currency_details.csv")
currency_details_data = currency_details_file.readlines()
print(currency_details_data)
countries = currency_details_data[0].strip().split(",")
currency_details_values = []
for currency_details_line in currency_details_data[4:]:
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
for currency_details_line in currency_details_data[56:]:
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



