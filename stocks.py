data = dict(info=[600, 630, 620], ril=[1430, 1490, 1567], mtl=[234, 180, 160])


def print_data(stock_data):
    for symbol, prices in stock_data.items():
        avg = round(sum(prices) / len(prices), 2)
        print(symbol, "=>", prices, "=>", avg)


user_input = str(input("Enter choice\n"))
if user_input == "print":
    print_data(data)
elif user_input == "add":
    stock = input("Enter Stock Name \n")
    price = float(input("Enter price \n"))
    if stock in data:
        data[stock].append(price)
    else:
        data[stock] = [price]
    print_data(data)
