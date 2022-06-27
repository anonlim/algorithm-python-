"""트리를 만들기 위한 노드를 생성"""
class Node:
    def __init__(self,data):
        self.l_child=None
        self.r_child=None
        self.data=data
"""트리구조를 만든다"""
def tree(key,r,i,j):
    k=r[i][j]
    if(k==0):
        return
    else:
        p=Node(key[k])
        p.l_child=tree(key,r,i,k-1)
        p.r_child=tree(key,r,k+1,j)
        return p
"""키를 찾는데 걸리는 평균시간이 최소가 되는 이진트리 구축"""
def optsearchtree(n,p,A,R):
    for diagonal in range(1,n):
        for i in range(1,n-diagonal+1):
            j=i+diagonal
            mindefault = 1000
            sumP=0
            for k in range(i,j+1):
                sumP+=p[k]

            for k in range(i,j+1):
                """mindefault가 갱신되면, 그 값에 sumP값도 들어가있으므로 이를 빼주고 최소값을 계산한다"""
                if (A[i][k-1]+A[k+1][j])<mindefault-sumP:
                    mindefault = A[i][k - 1] + A[k + 1][j]+sumP
                    A[i][j]=A[i][k-1]+A[k+1][j]+sumP
                    R[i][j]=k

    return A,R
"""전위순회로 출력한다"""
def printPreorder(root):
    if root!=None:
        print(root.data,end=" ")
        if root.l_child:
            printPreorder(root.l_child)
        if root.r_child:
            printPreorder(root.r_child)
"""중위순회로 출력한다"""
def printInorder(root):
    if root==None:
        return
    printInorder(root.l_child)
    print(root.data,end=" ")
    printInorder(root.r_child)

key=[" ","A","B","C","D","E","F","G","H"]
p=[0,1/8,1/8,1/8,1/8,1/8,1/8,1/8,1/8]

'''p=[0,1/15,2/15,3/15,4/15,5/15]'''
"""from fractions import Fraction
p=[0,Fraction(1,15),Fraction(2,15),Fraction(3,15),
   Fraction(4,15),Fraction(5,15)]"""
n=len(p)-1

a=[[0for j in range(0,n+2)]for i in range(0,n+2)]
r=[[0for j in range(0,n+2)]for i in range(0,n+2)]

"""a,와 r배열을 각각 초기값을 지정한다."""
for i in range(1,n+1):
    a[i][i-1]=0
    a[i][i]=p[i]
    r[i][i]=i
    r[i][i-1]=0
a[n+1][n]=0
r[n+1][n]=0

a,r=optsearchtree(n,p,a,r)
print(*a,sep='\n')
print()
print(*r,sep='\n')

root=tree(key,r,1,n)

printInorder(root)
print()
printPreorder(root)