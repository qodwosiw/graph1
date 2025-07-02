from collections import deque

def bfs_directed(graph, start):
    visited = {node: False for node in graph}
    distance = {node: float('infinity') for node in graph}
    predecessor = {node: None for node in graph}

    queue = deque([start])
    visited[start] = True
    distance[start] = 0

    while queue:
        vertex = queue.popleft()
        for neighbor in graph[vertex]:  # 遍历有向边指向的顶点
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
                distance[neighbor] = distance[vertex] + 1
                predecessor[neighbor] = vertex

    return distance, predecessor

# 示例：有向图的邻接表表示
directed_graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': ['C'],
    'E': []
}

start_vertex = 'A'
distances, predecessors = bfs_directed(directed_graph, start_vertex)

print("距离:", distances)
print("前驱节点:", predecessors)