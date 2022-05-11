inventor = {#dicionario
  'ouro' : 500,
  'bolsa' : ['chave', 'celular', 'dinheiro'],
  'mochila' : ['notebook','leitor', 'agenda','biscoito']
}
print(inventor)

inventor['animais'] = ['macaco', 'girafa', 'elefante']#add lista dicionario;
inventor['saco'] = ['maça', 'rubi', 'preguiça']
inventor['mochila'].sort()#ordem alfabetica lista dentro dicionario;
inventor['bolsa'].sort()
inventor['saco'].remove('rubi')#removendo item lista dentro dicionario;
print(inventor)
