
def getDataSetFractal () :

    return


def listRem (l0,l1):
#    len = len(l0)
    l0n,l1n=[],[]
    eps = 0.001
    val = 0
    for i in range(0,len(l1)):
        v = l1[i]
        if abs(v - val) > eps :
#            print (v-val)
            l1n.append(l1[i])
            l0n.append(l0[i])
        val = v
    return l0n, l1n
