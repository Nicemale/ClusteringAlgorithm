#computing all things :



# computing distance matrix of D
def c_distance_matrix(D):
    """
    computing distance matrix of set D
    :param D:
    :return: Distance matrix
    """
    D_len = len(D)
    D_distance = [([0] * D_len) for i in range(D_len)]
    for i in range(D_len):
        for j in range(i+1,D_len):
            x1 = D[i+1][0]
            y1 = D[i+1][1]
            x2 = D[j+1][0]
            y2 = D[j+1][1]
            D_distance[i][j] = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
            D_distance[j][i] = D_distance[i][j]
    return D_distance

def c_OMEGA_neigPtOfCoreObj(D_distance,epsilon,MinPts):
    OMEGA = []
    neigPtOfCoreObj = {}
    for i in range(len(D_distance)):
        numOfPt = 0
        neighPoints = []
        for j in range(len(D_distance[0])):
            if D_distance[i][j] <= epsilon:
                numOfPt += 1
                neighPoints.append(j)
        # print("第%d行，共有%d个满足条件的点" % (i,numOfPt) )
        if numOfPt >= MinPts:
            OMEGA.append(i)
            neigPtOfCoreObj[i] = neighPoints
    #print(OMEGA)
    return (OMEGA,neigPtOfCoreObj)

#judge the point whether a directly density-reachable point:
def is_ddrp(point):
    pass

@DeprecationWarning
def is_coreObjectPoint(point):
    """
    judege the point whether a core object point
    :param point:
    :return:
    """
    pass
@DeprecationWarning
def find_neighPoint(point):
    """
    find out the poitn's neighbor points
    :param point:
    :return: form like --> [p1,p2...]
    """

    pass

if __name__ == "__main__":
    D_distance = [([0] * 2) for i in range(2)]
    c_distance_matrix(D_distance)
