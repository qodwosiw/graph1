import networkx as nx
from collections import defaultdict


# 1. 图的录入（手动构建或从文件读取）
def build_graph():
    """手动构建一个无向图示例"""
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    return graph


# 2. 转换为NetworkX图对象
def convert_to_networkx(graph):
    G = nx.Graph()
    for node in graph:
        for neighbor in graph[node]:
            G.add_edge(node, neighbor)
    return G


# 3. 计算中心性指标
def calculate_centralities(G):
    # 度中心性
    degree_centrality = nx.degree_centrality(G)

    # 接近中心性
    closeness_centrality = nx.closeness_centrality(G)

    # 介数中心性
    betweenness_centrality = nx.betweenness_centrality(G)

    return degree_centrality, closeness_centrality, betweenness_centrality


# 4. 主程序
if __name__ == "__main__":
    # 构建图
    graph_data = build_graph()
    G = convert_to_networkx(graph_data)

    # 计算中心性
    degree, closeness, betweenness = calculate_centralities(G)

    # 打印结果
    print("节点\t度中心性\t接近中心性\t介数中心性")
    print("-" * 50)
    for node in G.nodes():
        print(f"{node}\t{degree[node]:.4f}\t\t{closeness[node]:.4f}\t\t{betweenness[node]:.4f}")