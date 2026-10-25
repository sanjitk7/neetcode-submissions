class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i: [] for i in range(n)}

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visited = set()

        def dfs(cur, prev):
            if cur in visited: # loop
                return False
            
            visited.add(cur)
            
            for neigh in adj[cur]:
                if neigh == prev: # skip backtracking and flagging for loop
                    continue
                if not dfs(neigh, cur):
                    return False
            
            return True

        return dfs(0, -1) and n == len(visited)