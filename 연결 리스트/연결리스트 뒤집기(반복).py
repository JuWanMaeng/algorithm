class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        node=head
        prev=None
        
        while node:
            new_node,node.next=node.next,prev
            prev,node=node,new_node
        return prev