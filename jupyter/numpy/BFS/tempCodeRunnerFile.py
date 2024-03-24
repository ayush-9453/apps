from collections import deque
graph = { 
    '5':['3','7'],
    '3':['2','4'],
    '7':['8'],
    '2':[],
    '4':['8'],
    '8':[]
}
visit = []
queue =[]

def bfs(visit , graph , node):
    visit.append(node)
    queue.append(node)

    while queue: 
        n = queue.popleft()