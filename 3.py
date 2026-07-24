import heapq

# =====================================================
# UNION-FIND (Disjoint Set) FOR KRUSKAL
# =====================================================
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])   # Path Compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return False

        if self.rank[rootX] < self.rank[rootY]:
            rootX, rootY = rootY, rootX

        self.parent[rootY] = rootX

        if self.rank[rootX] == self.rank[rootY]:
            self.rank[rootX] += 1

        return True


# =====================================================
# KRUSKAL'S ALGORITHM
# =====================================================
def kruskal(n, edges):

    edges.sort()

    uf = UnionFind(n)

    mst = []
    total_cost = 0

    for weight, u, v in edges:

        if uf.union(u, v):

            mst.append((u, v, weight))
            total_cost += weight

            if len(mst) == n - 1:
                break

    return mst, total_cost


# =====================================================
# PRIM'S ALGORITHM
# =====================================================
def prim(n, graph, start=0):

    visited = [False] * n

    pq = [(0, start, -1)]

    mst = []
    total_cost = 0

    while pq:

        weight, node, parent = heapq.heappop(pq)

        if visited[node]:
            continue

        visited[node] = True

        if parent != -1:
            mst.append((parent, node, weight))
            total_cost += weight

        for neighbor, wt in graph[node]:
            if not visited[neighbor]:
                heapq.heappush(pq, (wt, neighbor, node))

    return mst, total_cost


# =====================================================
# GRAPH
# =====================================================

n = 7

edges = [

    (7, 0, 1),
    (5, 0, 3),
    (8, 1, 2),
    (9, 1, 3),
    (7, 1, 4),
    (5, 2, 4),
    (15, 3, 4),
    (6, 3, 5),
    (8, 4, 5),
    (9, 4, 6),
    (11, 5, 6)

]

graph = {i: [] for i in range(n)}

for weight, u, v in edges:
    graph[u].append((v, weight))
    graph[v].append((u, weight))


# =====================================================
# MAIN PROGRAM
# =====================================================

if __name__ == "__main__":

    print("=" * 50)
    print("MINIMUM SPANNING TREE ALGORITHMS")
    print("=" * 50)

    # Kruskal
    kruskal_mst, kruskal_cost = kruskal(n, edges.copy())

    print("\nKruskal's Algorithm")
    print("-" * 50)

    for u, v, w in kruskal_mst:
        print(f"Edge {u} ---- {v}   Weight = {w}")

    print(f"\nTotal Cost = {kruskal_cost}")

    # Prim
    prim_mst, prim_cost = prim(n, graph)

    print("\nPrim's Algorithm")
    print("-" * 50)

    for u, v, w in prim_mst:
        print(f"Edge {u} ---- {v}   Weight = {w}")

    print(f"\nTotal Cost = {prim_cost}")