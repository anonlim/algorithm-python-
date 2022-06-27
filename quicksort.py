#퀵정렬(conquer)
def quicksort(s,low,high):
    if(high>low):
        s,pivotpoint=partition(s,low,high)
        quicksort(s,low,pivotpoint-1)
        quicksort(s,pivotpoint+1,high)
#파티션(divide)
def partition(s,low,high):
    pivotitem=s[low]
    j=low
    global count
    for i in range(low+1,high+1):
        count += 1
        if(s[i]<pivotitem):
            j+=1
            s[i],s[j]=s[j],s[i]
    pivotpoint=j
    s[low],s[pivotpoint]=s[pivotpoint],s[low]
    return s,pivotpoint

'''s=[3,5,2,9,10,14,4,8]

quicksort(s,0,7)
print(s)
'''

import random
#원소가 n개인 배열 만드는 함수
def makearr(n):
    arr=[]
    i=0
    while i<n:
        arr.append(random.randrange(0,n+1))
        i+=1
    return arr

#원소 갯수가 100개 일때, 100set
count=0
i=0
while i<100:
    ar=makearr(100)
    quicksort(ar,0,99)
    i+=1
print(count/100)
a=count/100 #n이 100일때, 100set의 평균값을 a에 저장

#원소 갯수가 200개 일때, 200set
count=0
i=0
while i<200:
    ar=makearr(200)
    quicksort(ar,0,199)
    i+=1
print(count/200)
b=count/200  #n이 200일때, 200set의 평균값을 b에 저장

#원소 갯수가 300개 일때, 300set
count=0
i=0
while i<300:
    ar=makearr(300)
    quicksort(ar,0,299)
    i+=1
print(count/300)
c=count/300  #n이 300일때, 300set의 평균값을 c에 저장

count=0
i=0
while i<400:
    ar=makearr(400)
    quicksort(ar,0,399)
    i+=1
print(count/400)
d=count/400  #n이 400일때, 400set의 평균값을 d에 저장

#n이 100, 200, 300, 400일 때의 평균값을 이용하여 좌표를 찍음.
from matplotlib import pyplot as plt
x=[100,200,300,400]
y=[a,b,c,d]
plt.plot(x,y,'o')
plt.show()
