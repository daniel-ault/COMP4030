'''
	UUG is a simple unweighted, undirected graph data structure 
	for the purpose of testing graph algorithms.

	Usage:
		G = UUG()
		G.add(3,5)       # add edge (3,5)
		G.add(3,10)      # add edge (3,10)
		G[3,5]           # is True
		G[5,3]           # is True
		G[3,4]           # is False
		G.vertices       # the set {3,5,10}
		G.edges          # the list [(3,5), (3,10)]
		G.neighbors[3]   # the set {5,10}
'''
INFINITY = float("inf")

class UUG(object):
	def __init__(self):
		self._edges = {}
		self.vertices = set()
		self.neighbors = {}

	def add(self, i,j):
		self._edges[i,j] = self._edges[j,i] = True
		self.vertices.add(i)
		self.vertices.add(j)
		if i not in self.neighbors:
			self.neighbors[i] = set()
		if j not in self.neighbors:
			self.neighbors[j] = set()
		self.neighbors[i].add(j)
		self.neighbors[j].add(i)

	def __getitem__(self, edge):
		return edge in self._edges

	def __contains__(self, edge):
		return edge in self._edges

	@property
	def edges(self):
	    return [ (i,j) for (i,j) in self._edges.keys() if i<=j ]
	

'''
	WDG is a simple weighted, directed graph data structure 
	for the purpose of testing graph algorithms.

	Usage:
		G = WDG()
		G.add(3,5,100)       # add edge (3,5) with weight 100
		G[3,5]               # is 100
		G[5,3]               # is inf (positive infinity)
		G.vertices           # the set {3,5}
		G.edges              # the list [(3,5)]
		G.neighbors[3]       # the set {5}
'''
class WDG(object):
	def __init__(self):
		self._edges = {}
		self.vertices = set()
		self.neighbors = {}

	def add(self, i,j,weight):
		self._edges[i,j] = weight
		self.vertices.add(i)
		self.vertices.add(j)
		if i not in self.neighbors:
			self.neighbors[i] = set()
		self.neighbors[i].add(j)

	def __getitem__(self, edge):
		return self._edges[edge] if edge in self._edges else INFINITY

	def __contains__(self, edge):
		return edge in self._edges

	@property
	def edges(self):
	    return self._edges.keys()

