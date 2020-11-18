import numpy as np
import random
def generate_distance_matrix(n,mode='random'):
    # n: 城市个数
    if mode == 'random': # 随机产生距离矩阵
        distance_lowerbound = 1 # 城市之间允许的最小距离
        distance_upperbound = n ** 2 # 城市之间允许的最大距离
        distance = np.zeros((n,n),dtype='int') # 距离矩阵
        for i in range(1,n): # 第 2 列 ~ 最后一列，复杂度：O(n)
            for j in range(i): # 第 i 列 第 j + 1 个元素，复杂度：O(n)
                if j > 0:
                    distance_min = max([abs(distance[k,i] - distance[k,j]) for k in range(j)]) # 两边之差，复杂度：O(n)
                    distance_max = min([distance[k,i] + distance[k,j] for k in range(j)]) # 两边之和，复杂度：O(n)
                    distance[j,i] = random.randint(max(distance_min,distance_lowerbound),min(distance_max,distance_upperbound))
                else:
                    distance[j,i] = random.randint(distance_lowerbound,distance_upperbound) # 
        distance = distance + distance.T
        np.savetxt('distance.txt',distance)
    elif mode == 'load': # 从本地加载
        distance = np.loadtxt('distance.txt')
    return distance
if __name__=='__main__':
    n = 10
    distance = generate_distance_matrix(n)
    path = np.random.permutation(n)
