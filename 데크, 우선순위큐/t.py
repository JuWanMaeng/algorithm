import heapq     
import sys 

N=int(sys.stdin.readline())
maxheap,minheap=[],[]
for i in range(N):
    num=int(sys.stdin.readline())
    if not maxheap:
        heapq.heappush(maxheap,(-num,num))
    else:
        if num>maxheap[0][1]:
            heapq.heappush(minheap,num)

    if(len(minheap)>len(maxheap)+1):
        a=heapq.heappop(minheap)
        heapq.heappush(maxheap,(-a,a))
    if(len(maxheap)>len(minheap)+1):
        a=heapq.heappop(maxheap)
        heapq.heappush(minheap,a[1])
    
    print(maxheap[0][1])
    


