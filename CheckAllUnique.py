def wordd(palavra):
    list = []
    
    for h in palavra:
        list.append(h)

    for i in range(len(list)):
        count = list.count(list[i])
        if count > 1:
            print( "This word not have all unique word")

wordd( "palavra")
    
   
