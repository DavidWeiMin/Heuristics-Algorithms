from neighborhood import *
from generate_distance import *
import random
import math
import test_function
from path_show import *
def main():
    # generate TSP distance matrix
    n = 10 # 城市个数
    distance = generate_distance_matrix(n,mode='random')
    # parameter settings
    maxIteration = 1000 # 最大迭代次数
    # minIteration = 100 # 最小迭代次数
    t = [100 / i ** 2 for i in range(1,maxIteration + 1)] # temperature
    l = [100] * maxIteration # length of Markov chain
    x = list(range(len(distance))) + [0]
    obj = test_function.path_length(distance)
    obj_best = [float('inf')]
    iter_num = 0
    while 1:
        for i in range(l[iter_num]):
            neighbors = get_neighbor(x)
            y = neighbors[random.randint(0,len(neighbors) - 1)]
            if obj(y) < obj(x):
                x = y
            elif math.exp((obj(x) - obj(y)) / t[iter_num]) > random.uniform(0,1):
                x = y
        iter_num = iter_num + 1
        obj_best.append(obj(x))
        if iter_num >= maxIteration:
            break
        # elif iter_num >= minIteration and np.array(obj_best[:-minIteration]).std() < 1e-4:
        #     return True
    print(x)
    print(obj_best[-1])
    plot(distance,x)

main()
