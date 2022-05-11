n = [3, 5, 7]#lista

def double_list(x):#função que multiplica todos os item da lista por 2
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

print(double_list(n))