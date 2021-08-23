'''In this problem we have used heaps, heaps are priority queue, heap has the worst time complexity equals to O(h) where
h is the height of the tree and heappush and heappop functions have complexity of O(log(n))'''

from heapq import *

def closestPoints(points,k):
    heap = []

    for x,y in points:
        dist = -(x*x+y*y)

        if len(heap) == k:
            heappushpop(heap,(dist,x,y))

        else:
            heappush(heap,(dist,x,y))
