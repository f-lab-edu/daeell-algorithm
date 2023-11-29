class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        one = ""
        two = ""
        while l1:
            one += str(l1.val)
            l1 = l1.next if l1 else None
        while l2:
            two += str(l2.val)
            l2 = l2.next if l2 else None
        
        one = one[::-1]
        two = two[::-1]
        
        sum_num = str(int(one) + int(two))
        head = ListNode(0)
        curr = head
        for i in range(len(sum_num)-1, -1, -1):
            new_node = ListNode(sum_num[i])
            curr.next = new_node
            curr = new_node
    
        return head.next