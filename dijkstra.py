def dijkstra(n,W):
    '''length 업데이트 횟수'''
    NoC=0

    '''touch와 length를 초기화'''
    touch=[0for i in range(n)]
    length=[0for i in range(n)]
    for i in range(1,n):
        length[i]=W[0][i]

    F=set()

    for j in range(0,n-1):
        min=1000
        for i in range(1,n):
            '''최소값을 min에 저장하고 그 인덱스값을 vnear에 저장'''
            if(0<=length[i]and length[i]<min):
                min=length[i]
                vnear=i
        e=(touch[vnear],vnear)

        '''저장한 값을 set에 저장'''
        F.add(e)

        '''새로 추가된 노드값 업데이트'''
        for i in range(1,n):
            if(length[vnear]+W[vnear][i]<length[i]):
                length[i]=length[vnear]+W[vnear][i]
                touch[i]=vnear

        save_length[vnear]=length[vnear]
        length[vnear]=-1
        NoC += 1

    return F,save_length,NoC

inf=1000
w=[[0,15,4,11,5],[inf,0,inf,inf,inf],[inf,4,0,2,inf],[inf,inf,inf,0,inf],[inf,3,inf,1,0]]
n=5
f=set()
touch=n*[0]
length=n*[0]
save_length=n*[0]
NoC=0
f,save_length,NoC=dijkstra(n,w)

print(f)
print(save_length)
print(NoC)
