class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(head,prev=None):
            if not head:
                return prev
            new_head,head.next=head.next,prev
            return reverse(new_head,head)
        return reverse(head)