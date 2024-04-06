data = {'China': 143, 'India': 136, 'USA': 32, 'Pakistan': 21}


def print_data(country_data):
    for cntry, pop in country_data.items():
        print(cntry, "=>", pop)


user_input: str = input("Enter Something...")

if user_input.__eq__("print"):
    print_data(data)
elif user_input.__eq__("add"):
    country: str = input("Country Name")
    if str in data:
        print("Country already present")
    else:
        population = int(input("Enter Population"))
        data[country] = population
    print_data(data)
elif user_input.__eq__("remove"):
    country = str(input("Enter Country"))
    if country in data:
        del data[country]
    else:
        print("Country not present in dictionary")
    print_data(data)
elif user_input.__eq__("query"):
    country: str = input("Country Name")
    if country in data:
        print(data[country])
    else:
        print("Country not present in dictionary")

