found = False

def equality(a,b,c):
    if a == b or a == int(c) or b == int(c):
        return True
    else:
        return False

found = equality(6,5,"5")
print(found)