# dbscan algorithm --  density-based clustering
"""
Solution:
    input:
        1.sample set D;
        2.neighborhood (epsilon,MinPts)
    processing:

        -----ResultStorage-----
        ResultForm: [[cluster1],[cluster2]...[clusterN]]
        when the starting declare a list RESULT to store the cluster
        -----------------------

        ----INIT START----
        1.init core object set OMEGA = empty set
        2.computing the distance among all data points filling into two-dimensional matrix
        3.pick the point which meeting condition "neighborhood" into core set OMEGA
        ----INIT END----
        4.set cluster size K = 0 & unaccessed sample set TAO = D
        5.while OMEGA not empty then do :
        ----start do----
        6.create a set Visited to record accessed points and take out of the first element
        of OMEGA put into queue Q
            7.while queue Q not empty then do:
            --start do--
            8.take out the first element of Q and put it into set Visited then find its
            directly density-reachable points and then put into Q
            9.put unaccessed points into Q (which not in set Visited)
            --end do--
            10.cluster size K += 1 & current cluster is set Visited & RESULT.append(Visited)
            11.OMEGA = OMEGA - Visited & set Visited empty

    Ending:
        The list RESULT is the cluster classfied
"""

from DBSCAN import c_computing as c
# watermelon dataset
"""
    input the watermelon dataset:
    for i in range(int(input("number of datasets :"))):
        x = float(input("x:"))
        y = float(input("y:"))
        D[i+1] = (x,y)
    print(D)
"""

D = {1: (0.697, 0.46), 2: (0.774, 0.376), 3: (0.634, 0.264), 4: (0.608, 0.318), 5: (0.556, 0.215),
     6: (0.403, 0.237), 7: (0.481, 0.149), 8: (0.437, 0.211), 9: (0.666, 0.091), 10: (0.243, 0.267),
     11: (0.245, 0.057), 12: (0.343, 0.099), 13: (0.639, 0.161), 14: (0.657, 0.198), 15: (0.36, 0.37),
     16: (0.593, 0.042), 17: (0.719, 0.103), 18: (0.359, 0.188), 19: (0.339, 0.241), 20: (0.282, 0.257),
     21: (0.748, 0.232), 22: (0.714, 0.346), 23: (0.483, 0.312), 24: (0.478, 0.437), 25: (0.525, 0.369),
     26: (0.751, 0.489), 27: (0.532, 0.472), 28: (0.473, 0.376), 29: (0.725, 0.445), 30: (0.446, 0.459)}

RESULT = []


#TODO find out the CORE OBJECT POINT
#computing distance matrix
D_distance = c.c_distance_matrix(D)
#print(D_distance)

#input the neighborhood condition:
epsilon = float(input("input the epsilon:"))
MinPts = float(input("input the MinPts:"))
# pick the points from distance_matrix that metting the CORE OBJECT POINTS condition
# algorithm: {i | D_distance[i][j] < epsilon --> count + 1, count >= MinPts}
(OMEGA,neigPtOfCoreObj) = c.c_OMEGA_neigPtOfCoreObj(D_distance,epsilon,MinPts)
print(neigPtOfCoreObj)
import copy
OMEGA_cp = copy.deepcopy(OMEGA)

numOfCluster = 0
visitedVertext = []
clusterResult = {}
#print(visitedVertext.__contains__(1))
while len(OMEGA):
     curr_queue = []
     core_point = OMEGA.pop()
     curr_queue.append(core_point)
     currClass_points = [] # to store current class points
     # when curr_queue not empty, then do:
     while len(curr_queue):
          point = curr_queue.pop()
          if visitedVertext.__contains__(point)==False:
               currClass_points.append(point+1)
               visitedVertext.append(point)
               # if the point is core object, then do :
               if OMEGA_cp.__contains__(point):
                    OMEGA_cp.remove(point)
                    #find out its neighbor point append into curr_queue:
                    print("pointOrder is:",point)
                    neighPoints = neigPtOfCoreObj[point] # [p1,p2..]
                    while len(neighPoints):
                         curr_queue.append(neighPoints.pop())
               # when the point not a core object, release it
     if len(currClass_points) != 0:
          clusterResult[len(clusterResult) + 1] = currClass_points
#init OMEGA:
print(clusterResult)

#Draw pic：
import matplotlib.pyplot as plt

color = ['r', '#46ff00', '#00c7ff', '#082933']
x = []
y = []
size = []
for val in clusterResult.values():
    for i in range(len(val)):
        x.append(D[val[i]][0])
        y.append(D[val[i]][1])
    size.append(len(clusterResult))

curr_index = 0
c_index = 0
fig = plt.figure(num=1, figsize=(15, 8),dpi=80)
for val in clusterResult.values():
    start = curr_index
    end = start+len(val)
    plt.scatter(x[start:end:1],y[start:end:1],c=color[c_index],label="DBSCAN AG By Chinge Class{0}".format(c_index+1))
    curr_index = end
    c_index += 1
plt.legend()
plt.show()


#TODO 优化-->显示噪声点;








