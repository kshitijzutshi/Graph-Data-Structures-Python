'''
Time and Space Complexity:
n = number of nodes
e = number of edges
As we would have to traverse through every edge
Time Complexity = O(e)
Space Complexity = O(n)

'''

def hasPathDFT_Iterative(graph, src, dst):
    # Implement using DFT Iterative
    stack = [src]
    while len(stack) > 0:
        current = stack.pop()
        if current == dst:
            return True
        for neighbour in graph[current]:
            stack.append(neighbour)

def hasPathDFT_Recurssive(graph, src, dst):
    # Implement using DFT Iterative
    
    if src == dst:
        return True
    for neighbour in graph[src]:
        if hasPathDFT_Recurssive(graph, neighbour, dst) == True:
            return True


graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

print("Iterative method:")
print(hasPathDFT_Iterative(graph, 'f', 'k')) # True
print(hasPathDFT_Iterative(graph, 'j', 'f')) # False
print("Recursive method:")
print(hasPathDFT_Recurssive(graph, 'f', 'k')) # True
print(hasPathDFT_Recurssive(graph, 'j', 'f')) # False

