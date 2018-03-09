import math 

dfs_solver_result = []
dls_solver_result = []

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

def findCellNeigbors(maze, s):
	result = maze.get_neighbors(s)
	return result

def dls_helper_rec(maze, s, visited, depth, limit):
	visited[s[0]][s[1]] = True 
	dls_solver_result.append(s)
	if (s == maze.goal) or (depth == limit):
		return

	for node in findCellNeigbors(maze, s):
		if visited[node[0]][node[1]]==False:
			dls_helper_rec(maze, node, visited, depth+1, limit)

# depth-limited dfs
def rec_dls_solver(maze, limit):
	visited = []
	for i in range(len(maze.cells)):
		visited.append([])
		for j in range(len(maze.cells)):
			visited[i].append(False)
	dls_helper_rec(maze, maze.start, visited, 0, limit)
	return dls_solver_result

def dls_solver(maze, limit):
	depth = {}
	result = []
	visited = []
	for i in range(len(maze.cells)):
		visited.append([])
		for j in range(len(maze.cells)):
			visited[i].append(False)
	iterStack = Stack()

	iterStack.push(maze.start)
	depth[maze.start] = 1

	while(iterStack.isEmpty()==False):
		s = iterStack.pop()

		if(visited[s[0]][s[1]] == False):
			visited[s[0]][s[1]] = True
			result.append(s)
			if s == maze.goal:
				break
		if depth[s] == limit:
			return result
		for node in findCellNeigbors(maze, s):
			if visited[node[0]][node[1]]==False:
				iterStack.push(node)
				depth[node] = depth[s]+1

	return result

def iterative_dfs_solver(maze):
	
	limit = 1
	while True:
		dls_path = dls_solver(maze, limit)
		if maze.goal in dls_path:
			return dls_path
		else:
			dls_solver_result[:] = []
			limit += 1

def dfs_helper_rec(maze, s, visited):
	visited[s[0]][s[1]] = True 
	dfs_solver_result.append(s)
	if s == maze.goal:
		return

	for node in findCellNeigbors(maze, s):
		if visited[node[0]][node[1]]==False:
			dfs_helper_rec(maze, node, visited)


def rec_dfs_solver(maze):
	visited = []
	for i in range(len(maze.cells)):
		visited.append([])
		for j in range(len(maze.cells)):
			visited[i].append(False)
	dfs_helper_rec(maze, maze.start, visited)
	return dfs_solver_result

def dfs_solver(maze):
	result = []
	visited = []
	for i in range(len(maze.cells)):
		visited.append([])
		for j in range(len(maze.cells)):
			visited[i].append(False)
	iterStack = Stack()

	iterStack.push(maze.start)

	while(iterStack.isEmpty()==False):
		s = iterStack.pop()

		if(visited[s[0]][s[1]] == False):
			visited[s[0]][s[1]] = True
			result.append(s)
			if s == maze.goal:
				break

		for node in findCellNeigbors(maze, s):
			if visited[node[0]][node[1]]==False:
				iterStack.push(node)

	return result


def bfs_solver(maze):
	cells = maze.cells
	if len(cells)==0:
		print("nothing has been generated")
	queue = []
	visited = []
	for i in range(len(maze.cells)):
		visited.append([])
		for j in range(len(maze.cells)):
			visited[i].append(False)
	queue.append(maze.start)
	visited[maze.start[0]][maze.start[1]] = True
	goal = maze.goal
	result = []
	while queue:
		s = queue.pop(0)
		result.append(s)
		if s==goal:
			break
		for node in findCellNeigbors(maze, s):
			if visited[node[0]][node[1]]==False:
				queue.append(node)
				visited[node[0]][node[1]] = True

	return result


def astar_heuristic(maze, cell):
	answer = math.sqrt((maze.goal[0]-cell[0])*(maze.goal[0]-cell[0]) + (maze.goal[1]-cell[1])*(maze.goal[1]-cell[1]))
	return answer

def distance_between_us_and_node(curr, node):
	return math.sqrt((curr[0]-node[0])*(curr[0]-node[0]) + (curr[1]-node[1])*(curr[1]-node[1]))


def findMinValue(nodes = [], costs = {}):
	if len(nodes)==0:
		return (-1, -1)
	minNode = nodes[0]
	for thisNode in nodes:
		if costs[thisNode] < costs[minNode]:
			minNode = thisNode
	return minNode

def create_result_path(path = {}, curr = ()):
	result = []
	result.append(curr)
	while (curr in path.keys()):
		curr = path[curr]
		result.append(curr)
	return result[::-1]


def astar_solver(maze):
	path = {}
	evaluatedNodes = []
	discoveredNodes = []

	costToGetToNode = {}
	costToGetToFinish = {}

	for i in range(len(maze.cells)):
		for j in range(len(maze.cells)):
			costToGetToFinish[(i, j)] = math.inf 
			costToGetToNode[(i, j)] = math.inf

	
	discoveredNodes.append(maze.start)
	costToGetToNode[(maze.start[0], maze.start[1])] = 0
	costToGetToFinish[(maze.start[0], maze.start[1])] = astar_heuristic(maze, maze.start)


	while discoveredNodes:
		curr = findMinValue(discoveredNodes, costToGetToFinish)
		if curr == maze.goal:
			return create_result_path(path, curr)

		discoveredNodes.remove(curr)
		evaluatedNodes.append(curr)

		for node in findCellNeigbors(maze, curr):
			if node in evaluatedNodes:
				continue
			if node not in discoveredNodes:
				discoveredNodes.append(node)


			cost = costToGetToNode[curr] + distance_between_us_and_node(curr, node)

			if cost >= costToGetToNode[node]:
				continue 

			path[node] = curr
			costToGetToNode[node] = cost
			costToGetToFinish[node] = costToGetToNode[node] + astar_heuristic(maze, node)


