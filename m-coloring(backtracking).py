k=0
def m_coloring(i,vcolor):
    global k
    if promising(i,vcolor):
        '''vcolor[i]=노드의 색'''
        k+=1
        if i+1==n:
            print(vcolor)
        else:
            '''상태공간 트리형태로 재귀반복'''
            for color in range(1,m+1):
                vcolor[i+1]=color
                m_coloring(i+1,vcolor)
def promising(i,vcolor):
    switch=True
    j=0
    while(j<i and switch):
        '''인접행렬이거나(0)이면 인접x, 인접한색이 같을땐 false'''
        if(W[i][j] and vcolor[i]==vcolor[j]):switch=False
        j+=1
    return switch

n=5
W=[[0,1,1,0,1],[1,0,1,1,0],[1,1,0,1,0],[0,1,1,0,1],[1,0,0,1,0]]
vcolor=n*[0]
m=4
m_coloring(-1,vcolor)
'''노드의 갯수 출력'''
print(k)