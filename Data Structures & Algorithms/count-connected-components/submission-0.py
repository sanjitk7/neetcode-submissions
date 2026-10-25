class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # basically number of islands but in dictionary
        res, visited = 0, set()
        adj = {i:[] for i in range(n)}
        
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neigh in adj[node]:
                dfs(neigh)
        

        for node in range(n):
            if node not in visited:
                dfs(node)
                res +=1

        return res