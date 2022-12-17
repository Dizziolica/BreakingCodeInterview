def removeDup(palavra):
    list = []
    for i in palavra:
        if i not in list:
            list.append(i)
            
    palavra1 = ''.join(list)
    
    print(palavra1)
    print(palavra)
    
removeDup("aabbcc")
