def insertion_sort(array):
    for a in range(1,len(array)):
        for b in range(a,0,-1):
            if array[b-1]>array[b]:
                array[b-1],array[b]=array[b],array[b-1]
    return array

def quick_sort(array,start,end):
    if start>=end: return
    pivot=array[start]
    left, right=start+1,end

    while left<=right:
        while left<=end and array[left]<=array[pivot]:
            left+=1
        while right>start and array[right]>=array[pivot]:
            right-=1
        if left>right:
            array[right],array[pivot]=array[pivot],array[right]
        else:
            array[right],array[left]=array[left],array[right]
        quick_sort(array,start,right-1)
        quick_sort(array,right+1,end)