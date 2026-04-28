import heapq
from core.utils import get_neighbors, heuristic

def a_star(start, goal):
    pq = []
    heapq.heappush(pq, (heuristic(start, goal), 0, start, []))
    vis = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        key = tuple(tuple(r) for r in state)
        if key in vis:
            continue
        vis.add(key)

        if state == goal:
            return path + [state]

        for n in get_neighbors(state):
            heapq.heappush(pq, (g+1+heuristic(n, goal), g+1, n, path+[state]))

    return []