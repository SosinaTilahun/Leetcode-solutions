class Solution:
    def countCompleteComponents(self, n, edges):
        # Build graph
        graph = [[] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = [False] * n
        result = 0

        def dfs(node):
            visited[node] = True
            nodes = 1
            edge_count = len(graph[node])

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    sub_nodes, sub_edges = dfs(neighbor)
                    nodes += sub_nodes
                    edge_count += sub_edges

            return nodes, edge_count

        for i in range(n):
            if not visited[i]:
                nodes, edges_count = dfs(i)

                # Each edge counted twice
                edges_count //= 2

                # Check if component is complete
                if edges_count == nodes * (nodes - 1) // 2:
                    result += 1

        return result