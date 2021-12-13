import math
import csv

# first example
# x = [10.4, 10.7, 13.4, 22.9, 29.3, 29.3, 29.3, 29.3, 29.3, 24.8,
#      18.8, 18.1,  5.8,  1.7,  0.7,  0.7,  0.7,  0.7]
# y = [29.3, 29.3, 29.3, 29.3, 28.2, 24.2, 12.0, 11.3,  5.1,  0.7,
#       0.7,  0.7,  0.7,  0.7,  8.1, 16.7, 19.3, 19.7]
# connections = [11, 5, 15, 8, 13, 1, 17, 10, 3, 14, 7, 0, 16, 4, 9, 2, 12, 6]
# start = 0

# second example
x = [ 7.0, 17.9, 19.5, 23.1, 29.3, 29.3, 29.3, 29.3, 29.3, 27.1,
     23.2, 14.8,  6.2,  2.3,  0.7,  0.7,  0.7,  0.7]
y = [29.7, 29.7, 29.7, 29.7, 27.7, 23.6, 15.2,  6.7,  2.9,  0.7,
      0.7,  0.7,  0.7,  0.7,  7.7, 10.5, 12.0, 23.0]
connections = [11, 16, 9, 4, 3, 12, 17, 10, 15, 2, 7, 0, 5, 14, 13, 8, 1, 6]
start = 17



# exporting table of distances to tsv
# grid = []
# for i in range(len(x)):
    # line = []
    # for j in range(len(x)):
        # dist = math.sqrt((x[i] - x[j])**2 + (y[i] - y[j])**2)
        # line.append(round(dist, 2))
    # grid.append(line)
# with open('output.tsv', 'w') as tsvfile:
    # writer = csv.writer(tsvfile, delimiter='\t')
    # for i in range(len(x)):
        # writer.writerow(grid[i])



layertravel = 0
path = []
currentpos = start
used = [0]*len(x)

# nearest neighbor
for i in range(9):
    nextpos = connections[currentpos]
    path.append(currentpos)
    path.append(nextpos)
    used[currentpos] = 1
    used[nextpos] = 1
    if not 0 in used:
        break
    currentpos = nextpos
    bestdist = 100
    bestpos = 0
    for j in range(len(used)):
        if used[j] == 0:
            dist = math.sqrt((x[j] - x[currentpos])**2 + (y[j] - y[currentpos])**2)
            if dist < bestdist:
                bestdist = dist
                bestpos = j
    layertravel += bestdist
    currentpos = bestpos

print("Nearest neighbor length: " + str(layertravel))
print("Nearest neighbor path: " + str(path))



bestlayertravel = 10000
worstlayertravel = 0
bestpath = []

# brute force
def nextline(pos, newx, newy, used, travel, path):
    nextpos = connections[pos]
    used[pos] = 1
    used[nextpos] = 1
    path.append(pos)
    path.append(nextpos)
    if not 0 in used:
        global bestlayertravel
        global worstlayertravel
        global bestpath
        if travel < bestlayertravel:
            bestlayertravel = travel
            bestpath = path.copy()
            print(bestlayertravel)
        if travel > worstlayertravel:
            worstlayertravel = travel
    else:
        for p in range(len(newx)):
            if used[p] == 0:
                newtravel = travel + math.sqrt((newx[p] - newx[nextpos])**2 + (newy[p] - newy[nextpos])**2)
                nextline(p, newx, newy, used.copy(), newtravel, path.copy())

nextline(start, x, y, [0]*len(x), 0, [])

print("Optimal length: " + str(bestlayertravel))
print("Optimal path: " + str(bestpath))
print("Worst length: " + str(worstlayertravel))
