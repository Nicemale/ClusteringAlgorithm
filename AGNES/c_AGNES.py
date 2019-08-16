# AGNES : agglomerative nesting
from AGNES import c_hausdorff as c_ds
import matplotlib.pyplot as plt


plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.figure(figsize=(20, 17))
def find_closest_class(distance_matrix):
    """
    find the closest class and return two class order I and J
    :param distance_matrix: class distance matrix
    :return: two closest class order I and J
    """
    _row = len(distance_matrix)
    _col = len(distance_matrix)
    retI = 0
    retJ = 0
    minDis = float("inf")
    for i in range(_row-1):
        for j in range(i+1,_col):
            if distance_matrix[i][j] < minDis:
                minDis = distance_matrix[i][j]
                retI = i
                retJ = j
    # print("当前距离矩阵为：",distance_matrix)
    # print("当前dausdorff距离最近的两个类为：{0}--{1}".format(retI,retJ))
    return (retI,retJ)

def point_dist(p1,p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

#init the set:
def agnes_init(D):
    """
    init sample set D
    :param D: sample set like [(x1,y1),(x2,y2)...]
    :return:1. a data struct like {1:[[(x1,y1),(x2,y2)...]]} --> 1: Cluster count; Out layer: wrap all current clusters; Inner layer: wrap each cluster in current times
            2. the distance between all datapoints
    """
    clusterStruct = {}
    clusterStruct[1] = []
    for data in D:
        exemplar = []
        exemplar.append(data)
        # print("current class own point(s) is(are): ",exemplar)
        clusterStruct[1].append(exemplar)
    initPoints = clusterStruct[len(clusterStruct)].__len__()
    # print("clusterStruct is ",clusterStruct," current cluster count is :",initPoints)
    # create a two dimentions array to record distance between two point

    distance = [([0]*initPoints) for i in range(initPoints)]   # ** NOTICE **  distance is a distance matrix of class instead of two points.
    for i in range(initPoints-1):
        for j in range(i+1,initPoints):
            # print("j = ",j)
            distance[i][j] = point_dist(clusterStruct[1][i][0],clusterStruct[1][j][0])
            distance[j][i] = distance[i][j]

    return (distance,clusterStruct,initPoints)

if __name__ == "__main__":#(3,4),(4,5),(5,6),(6,7),,(2,8)
    # D = [(1,8),(1,10),(2,8),(8,2),(9,2),(9,4)]  #count of cluster :2  --> result:{1: [[(1, 8), (2, 8), (1, 10)], [(8, 2), (9, 2), (9, 4)]]}
    D = [(1,2),(9,11),(1,8),(1,10),(8,2),(9,2),(9,4),(3,4),(4,5),(5,6),(6,7),(2,8)]
    (distance_matrix,clusterStruct,initPoints_count) = agnes_init(D)
    k = int(input("count of cluster :"))
    q = initPoints_count
    while q > k :
        (i,j) = find_closest_class(distance_matrix)
        len_clusterStruct = len(clusterStruct)
        import copy as cp
        cp_clusterStruct = cp.deepcopy(clusterStruct)
        cp_clusterStruct[len_clusterStruct][i].extend(cp_clusterStruct[len_clusterStruct][j])
        cp_clusterStruct[len_clusterStruct].pop(j)
        clusterStruct[len_clusterStruct+1] = cp_clusterStruct[len_clusterStruct]
        distance_matrix.pop(j)
        for index in range(q-1):
            distance_matrix[index].pop(j)
        #update the distance_matrix
        distance_matrix = c_ds.c_distance_class(clusterStruct)
        q -= 1
    print("共迭代:",clusterStruct.__len__(),"次，迭代数据：",clusterStruct)
    if clusterStruct.__len__() % 3 == 0:
        subplot_row = clusterStruct.__len__() // 3
    else:
        subplot_row = clusterStruct.__len__() // 3 +1

    subplot_col = 3
    for i in range(clusterStruct.__len__()):
        color = ["r","g","b","k","m","c","y","#d9a882","#d98382","#d982cb","#9c82d9","#82a0d9"]
        curr_data = clusterStruct[i+1]
        class_count = curr_data.__len__()
        x = []
        y = []
        for j in range(class_count):
            for k in range(len(curr_data[j])):
                x.append(curr_data[j][k][0])
                y.append(curr_data[j][k][1])

            plt.subplot(subplot_row, subplot_col, i+1)
            plt.scatter(x,y,c=color[j],lw="1")
            plt.title("第{0}次迭代".format(i+1))
            x = []
            y = []

    plt.show()


