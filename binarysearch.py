def location (data,item,low, high):
    if(low>high):
        return 0
    else:
        mid=round((low+high)/2)
        if(item==data[mid]):
            return mid
        elif(item<data[mid]):
            return location(data,item,low,mid-1)
        else:
            return location(data,item,mid+1,high)

import random
def random_List(size):
    result=[]

    for v in range(size):
        result.append(random.randint(0,size))
    return result

import time
t=0
for i in range(1000):
    start=time.time()
    lst=random_List(128)
    location(lst,3,0,127)
    end=time.time()
    t+=end-start
print(t/1000)
t2=0
for i in range(1000):
    start=time.time()
    lst=random_List(256)
    location(lst,3,0,127)
    end=time.time()
    t2+=end-start
print(t2/1000)
t3=0
for i in range(1000):
    start=time.time()
    lst=random_List(256)
    location(lst,3,0,127)
    end=time.time()
    t3+=end-start
print(t3/1000)

'''관찰 결과 n이 128일 땐, 약 0.00007초 정도 소요되었고, n이 256일 땐, 약 0.0001333초, n이 512일 땐, 
약 0.0001334초 정도 소요되었다. 이진탐색의 시간복잡도는
 logN이기 때문에 n이 128일 때와 n이 256일 때보다, n이 256과 512일 때의 시간 증가 폭이 더 작음을 알 수 있다. '''