myUniqueList = []
myLeftovers = []
flag = False

def listAppend(d):
    if d not in myUniqueList:
        myUniqueList.append(d)
        flag = True
        print(flag)
        return flag
    else:
        myLeftovers.append(d)
        flag = False
        print(flag)
        return flag

listAppend(1)
print("Accepted=",myUniqueList)
print("Rejected=",myLeftovers)

listAppend(10)
print("Accepted=",myUniqueList)
print("Rejected=",myLeftovers)

listAppend(11)
print("Accepted=",myUniqueList)
print("Rejected=",myLeftovers)

listAppend(11)
print("Accepted=",myUniqueList)
print("Rejected=",myLeftovers)

listAppend(10)
print("Accepted=",myUniqueList)
print("Rejected=",myLeftovers)
