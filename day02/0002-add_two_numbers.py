class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        one = ""
        two = ""
        while l1:
            one += str(l1.val)
            l1 = l1.next
        while l2:
            two += str(l2.val)
            l2 = l2.next
        
        one = one[::-1]
        two = two[::-1]
        
        sum_num = str(int(one) + int(two))
        head = ListNode(sum_num[-1])
        curr = head
        for i in range(len(sum_num)-2, -1, -1):
            new_node = ListNode(sum_num[i])
            curr.next = new_node
            curr = new_node
    
        return head
    

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(-1)
        curr_node = dummy_head
        flag = 0
        while l1 or l2 or flag:
            tmp_one = l1.val if l1 else 0
            tmp_two = l2.val if l2 else 0
            tmp_sum = tmp_one + tmp_two + flag

            flag = tmp_sum // 10
            new_node = ListNode(tmp_sum % 10)

            curr_node.next = new_node
            curr_node = new_node

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy_head.next
