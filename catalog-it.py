tree = {}
nodes = set()
roots = []
for t in range(int(input())):
    child, parent = input().strip().split(",")
    nodes.add(child)
    if parent != "None":
        nodes.add(parent)
        tree.setdefault(parent, []).append(child)
    else:
        roots.append(child)
        tree.setdefault(parent, []).append(child)

for node in nodes:
    tree.setdefault(node, [])

for parent in tree:
    tree[parent] = sorted(tree[parent])

def dfs(node, depth):
    print("-" * depth + node.strip())
    for child in ((tree[node])):
        dfs(child, depth + 1)


for r in sorted(roots):
    dfs(r, 0)