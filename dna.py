a=['G','A','C','T','T','A','C','C']
b=['C','A','C','G','T','C','C','A','C','C']

m=len(a)
n=len(b)
table=[[0 for j in range(0,n+1)] for i in range(0,m+1)]
minindex=[[(0,0) for j in range(0,n+1)] for i in range(0,m+1)]

"""테이블의 맨오른쪽 세로줄에 대해서 값을 지정한다."""
for j in range(n-1,-1,-1):
    table[m][j]=table[m][j+1]+2

"""테이블의 맨아래 가로줄에 대해서 값을 지정한다."""
for i in range(m-1,-1,-1):
    table[i][n]=table[i+1][n]+2

"""나머지에 대해서 우하단 부터 역순으로 점화식에 따라 값을 지정한다."""
"""또한, 최소가 되는 지점의 좌표를 이용하여 minindex배열도 만든다."""
for i in range(m-1,-1,-1):
    for j in range(n-1,-1,-1):
        if a[i]==b[j]:penalty=0
        else:penalty=1
        minindex[i][j]=(i+1,j+1)
        x=table[i+1][j+1]+penalty
        y = table[i + 1][ j] + 2
        z=table[i][j+1]+2
        temp=[x,y,z]
        table[i][j]=min(temp)
        if table[i][j]==x:minindex[i][j]=(i+1,j+1)
        elif table[i][j]==y:minindex[i][j]=(i+1,j)
        else:minindex[i][j]=(i,j+1)
print(*table,sep="\n")
x=0
y=0

"""만든 minindex배열을 통해 DNA서열이 가장 잘 맞는 배열쌍을 -를 이용해 나타낸다."""
while (x<m and y<n):
    tx,ty=x,y
    print(minindex[x][y])
    (x,y)=minindex[x][y]
    if x==tx+1 and y==ty+1:
        print(a[tx]," ",b[ty])
    elif x==tx and y==ty+1:
        print(" - ", " ",b[ty])
    else:print(a[tx]," ", " - ")