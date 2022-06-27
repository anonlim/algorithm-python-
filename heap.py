import math

class heap(object):
    def __init__(self,S):
        self.S=S
        self.heapsize=len(S)-1
def siftUp(H,i):
    while(i>=2):
        if(H.S[i]>H.S[math.floor(i/2)]):
            temp=H.S[i]
            H.S[i]=H.S[math.floor(i/2)]
            H.S[math.floor(i/2)]=temp
        i=math.floor(i/2)
def add(H,k):
    H.S.append(k)
    H.heapsize+=1
    siftUp(H,H.heapsize)
#힙 구조인지 확인
def siftdown(H,i):
    siftkey=H.S[i]
    parent=i
    spotfound=False

    while(2*parent<=H.heapsize and not spotfound):
        if(2*parent<H.heapsize and H.S[2*parent]<H.S[2*parent+1]):
            largechild=2*parent+1
        else:largechild=2*parent
        if(siftkey<H.S[largechild]):
            H.S[parent]=H.S[largechild]
            parent=largechild
        else:spotfound=True
    H.S[parent]=siftkey

#루트값 반환
def root(H):
    keyout=H.S[1]
    H.S[1]=H.S[H.heapsize]
    H.heapsize=H.heapsize-1
    #맨밑에 데이터를 맨위로
    siftdown(H,1)
    return keyout

def heapsort(H, S):
    H=heap(H)
    #H배열을 한번에 heap으로 생성
    makeheap(H)
    removekeys(H,S)
    return S

def makeheap(H):
    n=H.heapsize
    for i in range(math.floor(n/2),0 ,-1):
        #depth가 i인 서브트리에 대해서 siftdown
        siftdown(H,i)

#제일 마지막에 있는 값을 가져옴
def removekeys(H,S):
    n=H.heapsize
    for i in range(n-1,-1,-1):
        S.append(root(H))
    return S
#1개씩 넣고 순서를 조정함
def makeheap1(a,H):
    n=len(a)
    k=0
    for i in range(n):
        H.S.append(a[i])
        k+=1
        siftUp(H,H.heapsize)
    return S

a=[0,11,14,2,7,6,3,9,5]
#방법2 모든 데이터를 트리에 넣은 상태에서 heap 구성
#일단 다 넣고 자리바꿈
b=heap(a)
makeheap(b)
print(b.S)
add(b,50)
print(b.S)
S=[]
s=heapsort(a,S)
print(s)
#방법1 데이터가 입력되는 순서대로 heap 매번 구성
#맨밑(depth제일 큰값)에 넣고 그때그때 자리바꿈
d=[]
c=heap(d)
d=makeheap1(a,c)
print(d)