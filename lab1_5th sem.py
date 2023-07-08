
def shortest_path(graph, node1, node2):
    path_list = [[node1]]
    path_index = 0
    # To keep track of previously visited nodes
    previous_nodes = {node1}
    if node1 == node2:
        return path_list[0]

    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = graph[last_node]
        # Search goal node
        if node2 in next_nodes:
            current_path.append(node2)
            return current_path
        # Add new paths
        for next_node in next_nodes:
            if not next_node in previous_nodes:
                new_path = current_path[:]
                print(new_path)
                new_path.append(next_node)
                print('new path',new_path)
                path_list.append(new_path)
                print('path list',path_list)
                # To avoid backtracking
                previous_nodes.add(next_node)
                print('previous node',previous_nodes)
        # Continue to next path in list
        path_index += 1
    # No path is found
    return []

graph = {}

graph[1] = {2, 5}
graph[2] = {1, 3, 5}
graph[3] = {2, 4}
graph[4] = {3, 5, 6}
graph[5] = {1, 2, 4}
graph[6] = {4}

A = shortest_path(graph, 1, 6)
print(A)