k=0
def sum_of_subsets(i,weight,total,include):
    global k
    if promising(i,weight,total):
        '''유망하고, weight값이 구하고자 하는 W와 같으면 포함된 값을 출력'''
        k+=1
        if weight==W:
            for j in range(0,n):
                if include[j]==0:print("no")
                else:
                    print(include[j])
        '''유망하지만, 아직 weight값이 W와 같지 않으면 재귀함수로 트리구조처럼
        계속 노드값을 더하며 W값과 맞는 값을 구함'''
        else:
            include[i+1]="yes"
            sum_of_subsets(i+1,weight+w[i+1],total-w[i+1],include)
            include[i+1]="no"
            sum_of_subsets(i+1,weight,total-w[i+1],include)
'''남은 값이 W와 더해질 때, 가능성이 있고 아직 weight값이 W를 넘지 않을때 유망함'''
def promising(i,weight,total):
    return weight+total>=W and (weight==W or weight+w[i+1]<=W)

n=5
w=[1,2,3,4,15]
W=15
print("items = ",w,"W = ",W)
include=n*[0]
total=0
for k in w:
    total+=k
sum_of_subsets(-1,0,total,include)
'''노드갯수 출력'''
print(k)
