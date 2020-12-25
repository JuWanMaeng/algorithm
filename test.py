def solution(number, k):
    count=0
    answer = ''
    stack=[number[0]]
    for i in range(1,len(number)):
        num=number[i]
        while len(stack)>0 and count!=k:
            
            if stack[-1]<num:
                stack.pop()
                count+=1
            else:
                break
            
        if stack:        
            if stack[-1]>=num and k-count==len(number)-i:
                count+=1
                continue

        stack.append(num)
    
    for s in stack:
        answer+=s

    return answer


print(solution('4177252841',4))