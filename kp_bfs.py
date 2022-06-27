import queue
class Node:
    def __init__(self,level,weight,profit,include):
        self.level=level
        self.weight=weight
        self.profit=profit
        self.include=include
def kp_BFS():
    global maxProfit
    global bestset
    global nodecnt #총 노드갯수
    global quemax #어느 한순간 큐에 저장되어있는 데이터의 개수 최댓값
    q=queue.Queue()
    temp=n*[0]
    #루트노드 생성
    v=Node(-1,0,0,temp)
    q.put(v)
    quemax=q.qsize()
    nodecnt+=1
    while(not q.empty()):
        v=q.get()
        #포함하는 경우 u를 자식노드로 생성
        u = Node(v.level+1, v.weight+w[v.level+1],
                 v.profit+p[v.level+1], v.include[:])
        nodecnt +=1
        u.include[u.level]=1
        #더 좋은해를 찾으면 재설정
        if (u.weight <= W and u.profit > maxProfit):
                maxProfit = u.profit
                bestset = u.include[:]
        if (compBound(u) > maxProfit) :
                q.put(u)
        #포함하지않는 경우 자식노드로 만듦
        u = Node(v.level+1, v.weight, v.profit, v.include)
        nodecnt +=1
        if (compBound(u) > maxProfit) :
            q.put(u)
        if(q.qsize()>=quemax):
            quemax=q.qsize()
'''bound 현단계에서 앞으로 얻을수있는 이익의 최대치계산'''
def compBound(u):
        if (u.weight >= W) :
            return 0
        else :
            result = u.profit
            j = u.level + 1
            totweight = u.weight
            while (j < n and totweight + w[j] <= W ):
               totweight = totweight+w[j]
               result = result+p[j]
               j+=1
            k = j
            #잘라서 넣음
            if (k < n) :
                result = result + ((W-totweight)*p[k]) /w[k]
            return result


n=4
W=6
p=[30,28,18,20]
w=[3,4,3,5]
include=[0]*n
maxProfit=0
bestset=n*[0]
nodecnt=0
kp_BFS()
print(bestset)
print(nodecnt)
print(quemax)