# Iterative method
def breadthFirstPrint(graph, source):
    queue = [source]
    while len(queue) > 0:
        current = queue.pop(0)
        print(current)
        for neighbour in graph[current]:
            queue.append(neighbour)


# Graph adjucency list
graph = {'A': ['B', 'C'],
         'B': ['D'],
         'C': ['E'],
         'D': ['F'],
         'E': [],
         'F': []}


print("Iterative method:")
breadthFirstPrint(graph, 'A') # Prints - A B C D E F