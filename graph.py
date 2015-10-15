import Queue

# Directed Graph
graph  = {
	"A":{"checked":False,"edges":["B","C"]},
	"B":{"checked":False,"edges":["C","D"]},
	"C":{"checked":False,"edges":["D","E"]},
	"D":{"checked":False,"edges":["E"]},
	"E":{"checked":False,"edges":["A"]},
	"F":{"checked":False,"edges":["E"]},
}

# Breadth First Approach
def hasPath(graph,start,end):
	q = Queue.Queue()
	visited = {}

	for i in graph[start]["edges"]:
		if i == end:
			return True
		else:
			q.put(i)

	graph[start]["checked"] = True

	while not q.empty():
		next = q.get()

		if not graph[next]["checked"]:
			for i in graph[next]["edges"]:
				if i == end:
					return True
				else:
					q.put(i)

		q.task_done()
		graph[next]["visited"] = True

	return False


print hasPath(graph,"A","E")