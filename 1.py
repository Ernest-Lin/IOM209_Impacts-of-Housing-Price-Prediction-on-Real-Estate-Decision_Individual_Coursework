import matplotlib.pyplot as plt
import networkx as nx

# 创建一个有向图
G = nx.DiGraph()

# 定义状态节点
states = [
    "Not Registered", "Registered", "Pending Activation", "Activated", "Expired Link"
]

# 定义状态之间的转变（转换）
transitions = [
    ("Not Registered", "Registered", "User registers"),
    ("Registered", "Pending Activation", "Activation email sent"),
    ("Pending Activation", "Activated", "User clicks activation link"),
    ("Pending Activation", "Expired Link", "Link expired"),
    ("Expired Link", "Pending Activation", "Request new activation email")
]

# 添加节点
G.add_nodes_from(states)

# 添加边（表示状态转换）
for (start, end, label) in transitions:
    G.add_edge(start, end, label=label)

# 布局设定：在状态图中使用不同的坐标
pos = {
    "Not Registered": (0, 0),
    "Registered": (1, 0),
    "Pending Activation": (2, 0),
    "Activated": (3, 0.5),
    "Expired Link": (3, -0.5),
}

# 绘制状态图
plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=10, font_weight="bold", arrows=True)

# 添加标签
edge_labels = {(start, end): label for (start, end, label) in transitions}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# 显示图形
plt.title("PBI 1.2 Email Activation Process - State Diagram")
plt.show()
