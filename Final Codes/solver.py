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
	depth +=1

	for node in findCellNeigbors(maze, s):
		if visited[node[0]][node[1]]==False:
			dls_helper_rec(maze, node, visited, depth, limit)

# depth-limited dfs
def dls_solver(maze, limit):
	visited = []
	for i in range(len(maze.cells)):
		visited.append([])
		for j in range(len(maze.cells)):
			visited[i].append(False)
	dls_helper_rec(maze, maze.start, visited, 0, limit)
	return dls_solver_result



def iterative_dfs_solver(maze):
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

def dfs_helper_rec(maze, s, visited):
	visited[s[0]][s[1]] = True 
	dfs_solver_result.append(s)
	if s == maze.goal:
		return

	for node in findCellNeigbors(maze, s):
		if visited[node[0]][node[1]]==False:
			dfs_helper_rec(maze, node, visited)


def dfs_solver(maze):
	visited = []
	for i in range(len(maze.cells)):
		visited.append([])
		for j in range(len(maze.cells)):
			visited[i].append(False)
	dfs_helper_rec(maze, maze.start, visited)
	return dfs_solver_result


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
		s = queue.pop()
		result.append(s)
		if s==goal:
			break
		for node in findCellNeigbors(maze, s):
			if visited[node[0]][node[1]]==False:
				queue.append(node)
				visited[node[0]][node[1]] = True

	return result


def astar_heuristic(maze, cell):
	return 0


def astar_solver(maze):
	"""
	based on my search there are a number of things that all A* algorithms have in common:
	closedSet --> set of nodes already evaluated
	openSet --> set of node we found but have not yet evaluated 
	I have constructed them as dictionaries with the keys being the nodes and the values being the cost of getting to that node
	"""
	openSet = {}
	openSet[maze.start] = 0

	return []








