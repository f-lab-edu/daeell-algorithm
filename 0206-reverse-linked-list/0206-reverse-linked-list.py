# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newNode = None
        currNode = head
        
        while currNode:
            nextNode = currNode.next
            currNode.next = newNode

            newNode = currNode
            currNode = nextNode
        
        return newNode