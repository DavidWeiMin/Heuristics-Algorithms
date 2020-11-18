import copy
def get_neighbor(i):
    neighbors = []
    for k in range(len(i) - 1):
        swap = copy.copy(i)
        if k < len(i) - 2:
            swap[k],swap[k + 1] = swap[k + 1],swap[k]
            swap[-1] = swap[0]
            neighbors.append(swap)
        else:
            swap[0] = swap[k]
            swap[k],swap[k + 1] = swap[k + 1],swap[k]
            neighbors.append(swap)
    return neighbors

if __name__ == '__main__':
    i = [0,1,2,3,0]
    neighbors = get_neighbor(i)
    for j in range(len(neighbors)):
        print(neighbors[j])



