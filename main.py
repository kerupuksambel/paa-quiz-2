import BellmanFord, Dijkstra
import random

vertices = 0
while vertices < 5:
	vertices = int(input("Enter the vertices of the graph (minimum 5) >> "))

graf = range(vertices)
graf_table = []
graf_existed = [[0 for column in range(vertices)] for row in range(vertices)]

is_negative = False

for src in graf:
	for dst in graf:
		poss = random.randint(0, 100)
		if poss < 50:
			if src != dst and graf_existed[src][dst] == 0:
				w = 0
				while w == 0:
					w = random.randint(-1, 5)
				
				if w < 0:
					is_negative = True
				graf_table.append([src, dst, w])
				graf_existed[src][dst] = 1
				graf_existed[dst][src] = 1


if is_negative:
	graph = BellmanFord.Graph(vertices)
	for t in graf_table:
		graph.addEdge(t[0], t[1], t[2])
	table = graph.BellmanFord(0)
	print("(This graph is directed graph.)")
else:
	graph = Dijkstra.Graph(vertices)
	for t in graf_table:
		graph.addEdge(t[0], t[1], t[2])
	table = graph.Dijkstra(0)
	print("(This graph is undirected graph.)")

print("Graph data : ")
for i in graf:
	print(i)

for t in graf_table:
	print(f'{t[0]} {t[1]} {t[2]}')
print('(You can use https://csacademy.com/app/graph_editor/ for graph visualization.)')

# print(table)

rand_choice = random.choice(list(range(1, vertices - 1)))
best = table[rand_choice]

guess = int(input("Guess what's the shortest path from Node 0 to {} >> ".format(rand_choice)))

if(guess != best):
	if(best == inf):
		print('Actually, there are no shortest path to {}.'.format(rand_choice))
	else:
		print("Close! The shortest is {}".format(best))
else:
	print("Correct!")