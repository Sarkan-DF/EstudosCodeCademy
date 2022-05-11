prices = {"banana": 4,"apple": 2,"orange": 1.5,"pear": 3}#dicionario simples
stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}

for key in prices:#laço q passa por todos item dicionario
  print (key)#imprime chave dicionario
  print ("price: %s" % prices[key])#imprime valor dicionario "prices"
  print ("stock: %s" % stock[key])#imprime valor dicionario "stock"
  print('')#imprime espaço