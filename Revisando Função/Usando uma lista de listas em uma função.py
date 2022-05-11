n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]#lista com 2 listas

def flatten(lists):#função q passa por todos item das 2 listas
    results = []
    for numbers in lists:
        for numbers in numbers:
            results.append(numbers)
    return results

print(flatten(n))