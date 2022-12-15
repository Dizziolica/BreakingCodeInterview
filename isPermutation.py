def isPermut( palavra , word2):
    count = 0
    for i in palavra:
        if i in word2:
            count += 1
    if count == len(word2):
        print("Is a Permutation")
    else: 
        print("Is not a Permutation")

isPermut("isis", "sisit")
