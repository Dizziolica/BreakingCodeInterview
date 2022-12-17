ef isReverse(palavra1, palavra2):
    if len(palavra1) == len(palavra2):
       word1 = []
        word2 = []
        for i in palavra1:
            word1.append(i)
        for j in palavra2:
            word2.append(j)
        
        word11 = ''.join(sorted(word1, key=str.lower))
        word22 = ''.join(sorted(word2, key=str.lower))
        
        if word11.lower() == word22.lower():
            print("Two words have same letters and len")
    else:
        print("They are different")
        
isReverse()
