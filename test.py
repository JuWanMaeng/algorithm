import collections
from typing import DefaultDict

def solution(phone_book):
    answer=True
    phone_book.sort(key=len)
    d=collections.defaultdict(int)
    for num in phone_book:
        if d:
            for key in d:
                lenn=len(key)
                if key==num[:lenn]:
                    return False
        d[num]=0
    
    return answer

print(solution(["119", "97674223", "1195524421"]))