def merge(h,m,U,V,S):
    i,j,k=0,0,0
    while(i<h and j<m):
        if(U[i]<V[j]):
            S[k]=U[i]
            i+=1
        else:
            S[k]=V[j]
            j+=1
        k+=1
    if(i>=h):
        while(j<m):
            S[k]=V[j]
            k+=1
            j+=1
    else:
        while(i<h):
            S[k]=U[i]
            k+=1
            i+=1
def mergesort(n,S):
    h=round(n/2)
    m=n-h
    U=[]
    V=[]
    for v in range(h):
        U.append(S[v])
    for v in range(m):
        V.append(S[h+v])
    if(n>1):
        mergesort(h,U)
        mergesort(m,V)
        merge(h,m,U, V, S)
import psutil
def memory_usage():
    p=psutil.Process()
    rss=p.memory_info().rss/2 **20
    print(rss,'MB')

lst=[8,3,15,2 ,9,1,5,7 ,4,16,10,11 ,12,13,6,14]
memory_usage()
mergesort(16,lst)
print(lst)
memory_usage()

'''탐구 결과 n 이 16인 리스트를 정렬한 프로그램에도 약 0.004MB가 사용되었음을 알 수 있다.
 따라서, 합병 정렬은 시간복잡도는 좋지만, 공간 복잡도가 효과적이지 않다고 볼 수 있다.'''