class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode):
        rev=None
        slow=fast=head
        while fast and fast.next:
            fast=fast.next.next
            rev,rev.next,slow=slow,rev,slow.next   #다중할당을 해야 풀림
        if fast:                     #연결리스트가 홀수인 경우
            slow=slow.next


        while rev and rev.val==slow.val:
            slow,rev=slow.next,rev.next
        return not rev
