def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        (2 -> 4 -> 3) + (5 -> 6 -> 4)
         |               |
        """
        prev = head = ListNode(0)
        carry = 0
        while l1 != None or l2 != None:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sum_val = (val1+val2+carry) % 10
            carry = (val1+val2+carry)//10
            head.next = ListNode(sum_val)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            head = head.next
            #print(sum_val)
        if carry:
            head.next = ListNode(carry)
        return prev.next
