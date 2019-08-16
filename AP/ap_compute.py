# -*- coding: utf-8 -*-
'''
compute r(i,k),a(i,k)

v0.0.1 this version could be drop into a endless loop
v0.0.2 maintain two matrix RESPONSIBILITY and AVALIABLE, the fn c_r and c_a update
       these matrix beside mutual computation
'''


class ag_compute:
    '''
     codeVer: 0.0.1
    '''
    def __init__(self,data_set,max_recursion):
        self.data_set = data_set
        self.recursion = max_recursion
        self.current_exec_times = 0
    def most_suitable_value(self,i,k):
        # compute all the values of a(i,k')+s(i,k') add into LIST then find the max
        temp_list = []
        for index in range(len(self.data_set)):
            if(index != k):
                temp_list.append(self.c_a(i,index)+self.s(i,index))
        return max(temp_list)

    def s(self,i,k):
        self.recursion += 1
        print("current recursion times:",self.current_exec_times)
        if(self.recursion < self.current_exec_times):
            return
        return -1*((self.data_set[i])**2-(self.data_set[k])**2)

    def c_r(self,i,k,):
        return self.s(i,k) - self.most_suitable_value(i,k)

    def c_a(self,i,k):
        temp_res = 0
        if(i == k):
            for index in range(len(self.data_set)):
                temp_r = self.c_r(index,k)
                if(index != k and temp_r > 0):
                    temp_res += temp_r
        else:
            temp_res = self.c_r(k,k)
            for index in range(len(self.data_set)):
                temp_r_diff = self.c_r(index,k)
                if(index != i and index != k and temp_r_diff > 0):
                    temp_res += temp_r_diff
            if(temp_res > 0):
                temp_res = 0
        return temp_res

if __name__ == "__main__":
    c = ag_compute([1,2],100)
    print(c.data_set[1])
    # print(c.c_r(1,2))
    for i in range(100):
        print(c.c_r(0,1))
        print(c.c_a(0,1))



