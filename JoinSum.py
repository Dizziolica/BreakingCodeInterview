def JoinSum(lista, lista2):
    
    numero1  = lambda list1: ''.join(map(str, list1))

    numero2 = lambda list2: ''.join(map(str, list2))

    result = int(numero1(lista)) + int(numero2(lista2))
    
    print(result)
    
removeDup([6,1, 7], [2, 9, 5])
