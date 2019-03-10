def trifeca(word):
    for i in range(len(word)-5):
        slice = word[i:i+6]
        # print(slice)
        if slice[0] == slice[1] and slice[2] == slice[3] and slice[4] == slice[5] :
            return True
    
    return False
