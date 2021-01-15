import copy
import random
def get_neighbor(i):
    neighbor = copy.deepcopy(i)
    index = random.randint(1,len(i) - 2)
    # if index != len(i) - 1:
    neighbor[index],neighbor[index + 1] = neighbor[index + 1],neighbor[index]
    # else:
    #     neighbor[index],neighbor[0] = neighbor[0],neighbor[index]
    # for k in range(len(i) - 1):
    #     swap = copy.copy(i)
    #     if k < len(i) - 2:
    #         swap[k],swap[k + 1] = swap[k + 1],swap[k]
    #         swap[-1] = swap[0]
    #         neighbors.append(swap)
    #     else:
    #         swap[0] = swap[k]
    #         swap[k],swap[k + 1] = swap[k + 1],swap[k]
    #         neighbors.append(swap)
    # neighbor = neighbors[random.randint(0,len(neighbors) - 1)]
    return neighbor

if __name__ == '__main__':
    i = list(range(12))
    neighbor = get_neighbor(i)
    print(neighbor)