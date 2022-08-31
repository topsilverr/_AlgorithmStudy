# 연결 정보만 저장
# 빈 배열 => 노드가 1부터 시작하므로 배열을 이용하려면 노드 0이 필요함
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

visited=[False]*9

def dfs(graph,n,visited):
	visited[n]=True
	print(n,end=' ')
	for i in graph[n]:
		if visited[i]!=True:
			dfs(graph,i,visited)

dfs(graph,1,visited)