from collections import deque

graph=[
				[],
				[2,3,8],
				[1,7],
				[1,4,5],
				[3,5],
				[3,4],
				[7],
				[2,6,8],
				[1,7]
			]
visited = [False] * 9

def bfs(graph,n,visited):
	queue=deque([n])
	visited[n]=True
	while queue:
		v=queue.popleft()
		print(v,end=' ')
		for i in graph[v]:
			if visited[i]!=True:
				queue.append(i)
				visited[i]=True

bfs(graph,1,visited)