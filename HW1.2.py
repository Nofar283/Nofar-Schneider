def check_palindrome():
    for i in range(100000,999999):
        stri = str(i)
        four = stri[2:6] 
        if not checkp(four):
            continue
        i1 = i+1
        one = str(i1)
        five = one[1:6]
        if not checkp(five):
            continue
        i2 = i1+1
        two = str(i2)
        middle = two[1:5]
        if not checkp(middle):
            continue
        i3=i2+1
        three = str(i3)
        if len(three) > 6:
            continue
        if not checkp(three):
            continue
        print(i)

def checkp(my_str):
    l = len(my_str)
    pair = l//2
    for i in range(pair):
        if not my_str[i] == my_str[l-i-1]:
            return False
    return True


check_palindrome()
