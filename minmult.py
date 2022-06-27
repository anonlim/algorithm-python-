'''행렬을 i번째 부터 j번째까지 곱하는 과정에서
최소의 계산을 하게하는 계산법 출력'''
def order(p,i,j):
    if(i==j):
        print("A",i,end="")
    else:
        '''k를 기준으로 나누며, 재귀함수를 통해 반복함'''
        k=p[i][j]
        print("(",end="")
        order(p,i,k)
        order(p,k+1,j)
        print(")",end="")

'''행렬 i부터 j까지 계산하는데 드는 최소 계산수를 
m행렬에 만듦'''
def minmult(n,d,p):
    m = [[0 for j in range(1, n + 2)] for i in range(1, n + 2)]

    for diagonal in range(1,n):
        for i in range(1,n-diagonal+1):
            j=i+diagonal
            minLim=1000
            for k in range(i,j):
                minnum=m[i][k]+m[k+1][j]+d[i-1]*d[k]*d[j]
                if(minnum<minLim):
                    minLim=minnum
                    p[i][j]=k
                    m[i][j]=minLim
    return m
n=7
d=[3,5,4,6,7,2,3,4]
n1=6
d1=[5,2,3,4,6,7,8]
p=[[0for j in range (1,n+2)]for i in range(1,n+2)]

m=minmult(n,d,p)
'''2차원 행렬을 출력함'''
print(*m,sep='\n')
print()
print(*p,sep='\n')
order(p,1,6)