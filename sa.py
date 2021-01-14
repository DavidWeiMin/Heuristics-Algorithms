from neighborhood import *
from generate_distance import *
import random
import math
import test_function
from path_show import *

def main():
    # generate TSP distance matrix
    n = 40 # 城市个数
    distance = generate_distance_matrix(n,mode='load')
    # parameter settings
    maxIteration = 1000 # 最大迭代次数
    # minIteration = 100 # 最小迭代次数
    t = [100 * 0.95 ** i for i in range(1,maxIteration + 1)] # temperature
    l = [100] * maxIteration # length of Markov chain
    x = list(range(len(distance))) # 初始解
    obj = test_function.path_length(distance) # 目标函数
    obj_best = [float('inf')] # 记录最优目标函数值
    x_best = [x] # 记录最优解
    iter_num = 0 # 迭代次数
    while 1:
        for i in range(l[iter_num]):
            y = get_neighbor(x) # 在解 i 的邻域内随机产生新解
            if obj(y) < obj(x): # 新解更优，直接接受
                x = y
            elif math.exp((obj(x) - obj(y)) / t[iter_num]) > random.uniform(0,1): # 旧解更优，以概率接受
                x = y
            if obj(x) < obj_best[-1]: # 如果新解比历史最优更优
                obj_best.append(obj(x)) # 记录访问过的最优目标函数
                x_best.append(x) # 记录访问过的最优解
        iter_num = iter_num + 1 # 迭代次数 +1
        if iter_num >= maxIteration:
            break
    print(x)
    print(obj_best[-1])
    # plot(distance,x)

main()
