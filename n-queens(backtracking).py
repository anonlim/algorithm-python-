node=0
ans=0
def queens(n,i,col):
    '''전역변수로 설정하여 함수가 호출될때마다 node값 +1'''
    global node,ans
    node += 1
    '''스위치 값이 true일때만 실행'''
    if(promising(i,col)):
        if(i==n-1):
            print(col)
            ans+=1
            '''전역변수로 설정하여 조건 해당될 때마다 해의 값 +1'''

        else:
            for j in range(0,n):
                col[i+1]=j
                '''재귀함수로 구현'''
                queens(n,i+1,col)
    return node
def promising(i,col):
    k=0
    '''퀸이 충돌하면 false, 안하면 true'''
    switch=True
    while(k<i and switch):
        '''같은 column, 같은 대각인지 확인'''
        if(col[i]==col[k]) or (abs(col[i]-col[k])==i-k):
            switch=False
        k+=1
    return switch

n=7
col=n*[0]
queens(n,-1,col)

print(ans)
print(node)