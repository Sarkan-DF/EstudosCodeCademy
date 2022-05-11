prices = {"banana": 4,"apple": 2,"orange": 1.5,"pear": 3}
stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}

for key in prices:
    if key == "banana":
        print("Banana")
        print('Prices: %s' % prices[key])
        print('Stock: %s' % stock[key])
        print("")
    elif key == "apple":
        print("apple")
        print('Prices: %s' % prices[key])
        print('Stock: %s' % stock[key])
        print("")
    elif key == "orange":
        print("orange")
        print('Prices: %s' % prices[key])
        print('Stock: %s' % stock[key])
        print("")
    else:
        print("pear")
        print('Prices: %s' % prices[key])
        print('Stock: %s' % stock[key])
        print("")