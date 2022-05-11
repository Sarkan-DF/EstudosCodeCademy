prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}#dicionario simples
stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}

total = 0#zerando variavel
for key in prices:#laço q passa por todos item dicionario
    print(prices[key] * stock[key])#multipli valor pricis por stock imprimindo
    total += prices[key] * stock[key]'''incrementando a variavel total com a
                                        multiplicação de prices por stock'''

print("O total em estoque e: %s" % total)#imprimindo total