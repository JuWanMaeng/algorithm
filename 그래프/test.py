import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0]<K and len(scoville)>1:
        answer+=1
        num1=heapq.heappop(scoville)
        num2=heapq.heappop(scoville)
        num=num1+num2*2
        heapq.heappush(scoville,num)
        

    if scoville[0]<K:
        return -1
    

    return answer

a=[0,0,0,0,0]
print(solution(a,1))
