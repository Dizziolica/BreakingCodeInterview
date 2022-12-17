def CountRept(palavra):
    list = []
    
    
    for i in range(len(palavra)):
        if palavra[i] not in list:
            number = palavra.count(palavra[i])
            list.append(palavra[i])
            list.append(number)
        finalword = "".join(map(str, list))
        print(finalword)
CountRept("aabbccdd")
