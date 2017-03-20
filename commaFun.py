
def listify(l):
    newList = ''
    
    for i in range(len(l)):
        if (i == (len(l) - 2)):
            newList += l[i] + ', and '
        elif (i == len(l) - 1):
            newList += l[i] + '.'
        else:
            newList += l[i] + ', '
            
    return newList

