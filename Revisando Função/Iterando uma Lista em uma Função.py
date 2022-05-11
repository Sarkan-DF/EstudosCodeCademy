n = [3, 5, 7]#lista

def total(numbers):#função que soma todos itens da lista
    result = 0
    for i in range(0, len(numbers)):
        result = result + numbers[i]
    return result

print(total(n))