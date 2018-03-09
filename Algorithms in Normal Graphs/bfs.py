import networkx as nx 
import matplotlib.pyplot as plt

class Graph:
	def __init__(self):
		self.G = nx.Graph()

	def generate_graph(self, numNodes):
		for x in range(numNodes):
			self.G.add_node(x)

		for i in range(numNodes):
			for j in range(numNodes):
				if (i%5==3 and j%3==2) or (i%4==2 and j%2==1):
					self.G.add_edge(i, j)

	def BFS(self, startingNode):
		print("Running BFS from "+startingNode+" ...")
		s = startingNode
		s = int(s)
		all_nodes = self.G.nodes()
		visited = [False]*len(all_nodes)

		queue = []
		queue.append(s)
		visited[s] = True

		while queue:
			s = queue.pop()
			print("Just Poped: "+str(s))
			print("Current Queue: "+str(queue))
			for x in self.G.neighbors(s):
				y = int(x)
				if visited[y]==False:
					queue.append(x)
					visited[y] = True

	def getAllNodes(self):
		return self.G.nodes()

	def printGraph(self):
		res = nx.draw(self.G, with_labels = True)
		plt.savefig('graph.png')
		plt.show()


def testFucn():
	myGraph = Graph()
	myGraph.generate_graph(10)
	print("The nodes are: "+str(myGraph.getAllNodes()))
	startingNode = input("Starting Node: ")
	myGraph.BFS(startingNode)
	myGraph.printGraph()

if __name__ == '__main__':
	testFucn()