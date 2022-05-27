# Iterative Method
def depthFirstPrint(graph, source):
    # We use the python list to implement a stack
    # initialize the stack with source
    stack = [source]
    # Perform DFT while the stack is not empty
    while len(stack) > 0:
        current = stack.pop()
        print(current)
        for neighbour in graph[current]:
            stack.append(neighbour)

# Recursive Method
def depthFirstPrintRecursive(graph, source):
    print(source)
    for neighbour in graph[source]:
        depthFirstPrintRecursive(graph, neighbour)


graph = {'A': ['B', 'C'],
         'B': ['D'],
         'C': ['E'],
         'D': ['F'],
         'E': [],
         'F': []}


print("Iterative method:")
depthFirstPrint(graph, 'A') # Prints - A C E B D F
print("Recursive method:")
depthFirstPrintRecursive(graph, 'A') # Prints - A B D F C E