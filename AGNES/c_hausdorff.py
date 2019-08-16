# computing hausdorff distance
def c_hd(X,Y):
    """
    compute single-way distance of set x and y
    :param X: a set like [(x1,y1),(x2,y2)...]
    :param Y: a set
    :return: single-way distance of set x and y
    """
    res = []
    temp_res = []
    for x in X :
        for y in Y:
            distance = (x[0] - y[0])**2 + (x[1] - y[1])**2
            temp_res.append(distance)
        temp_res.sort()
        res.append(temp_res[0])
        temp_res.clear()
    res.sort()
    return  res.pop() # the Kth one is the hd(x,y)
def c_Hd(X,Y):
    """
    compute two-way distance of set x and y
    :param X: a set
    :param Y: a set
    :return:  two-way distance of set x and y
    """
    return max(c_hd(X,Y),c_hd(Y,X))

def c_distance_class(D):
    currentClass = D[len(D)]
    currentClass_len = len(currentClass)
    distance = [([0]*currentClass_len) for i in range(currentClass_len)]
    for i in range(currentClass_len-1):
        for j in range(i+1,currentClass_len):
            distance[i][j] = c_Hd(currentClass[i],currentClass[j])
            distance[j][i] = distance[i][j]
    return  distance

if __name__=="__main__":
    X = [(1,20),(2,25)]
    Y = [(1,15),(2,5),(3,17)]
    res = c_Hd(X,Y)
    print("final res is :",res)

    m = [[0, 8, 18], [8, 0, 2], [18, 2, 0],[18, 2, 0]]
    print(len(m[0]))
