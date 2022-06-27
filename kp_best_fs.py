import queue
class Node:
    def __init__(self,level,weight,profit,bound,include):
        self.level=level
        self.weight=weight
        self.profit=profit
        self.include=include
        self.bound=bound
    def __lt__(self, other):
        return self.bound<other.bound

def kp_Best_FS():
    global maxProfit
    global bestset
    temp=n*[0]
    v=Node(-1,0,0,0.0,temp)
    #최소힙 구조로 역순으로 q선언
    q=queue.PriorityQueue()
    maxProfit=0
    v.bound=compBound(v)
    q.put((v.bound,v))

    while(not q.empty()):
        v.bound,v=q.get()
        #u를 v의 자식노드로 만듦 (다음 아이템 포함할때)
        if(v.bound<maxProfit):
            u=Node(0,0,0,0,temp)
            u.level=v.level+1
            u.weight=v.weight+w[u.level]
            u.profit=v.profit+p[u.level]
            u.include=v.include[:]
            u.include[u.level]=1
            u.bound=compBound(u)
            #bestset의 순간 값을 include에 저장
            if(u.weight<=W and u.profit>maxProfit):
                maxProfit = -u.profit
                bestset = u.include[:]
            # u를 v의 자식노드로 만듦 (다음 아이템 포함x일때)
            if (u.bound < maxProfit):
                q.put((u.bound, u))
            u = Node(0, 0, 0, 0.0, temp)
            u.weight = v.weight
            u.profit = v.profit
            u.include = v.include[:]
            u.level = v.level + 1
            u.bound = compBound(u)
            if (u.bound < maxProfit):
                q.put((u.bound, u))
'''bound 현단계에서 앞으로 얻을수있는 이익의 최대치계산'''
def compBound(u):
    if u.weight>=W:
        return 0
    else:
        result = u.profit
        j = u.level+1
        totweight = u.weight
        while( j < n and totweight + w[j] <= W) :
            totweight += w[j]
            result += p[j]
            j += 1
        k = j
        if ( k < n ) :
            result = result + ((W-totweight)*p[k])/w[k]
        return -result
n=4
W=16
p=[40,30,50,10]
w=[2,5,10,5]
include=[0]*n
maxProfit=0
bestset=n*[0]
kp_Best_FS()
print(bestset)
print(maxProfit)