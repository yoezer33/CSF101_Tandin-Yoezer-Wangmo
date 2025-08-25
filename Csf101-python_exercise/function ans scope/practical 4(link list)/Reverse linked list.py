class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def reverseList(head):
        prev = None
        current = head
        while current is not None:
            next_temp = current.next
            current.next = prev
            pre = current
            current = next_temp
        return prev
        
    def ___init__(self, val=0, next=None):
            self.val = val
            self.next = next
    def mergeTwoLisits(list1: ListNode, list2: ListNode) -> ListNode:
         dummy = ListNode(0)
         current = dummy
         while list1 and list2:
            if list1.val <= list2.val:
                   current.next = list1list1 = list1.next
            else:
                 current.next = list2
                 list2 = list2.next
                 current = current.next
            if list1:
                 current.next = list1
            if list2:
                 current.next = list2
    
            return dummy.next

#leetcode
## Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        previous = None
        current = head 
        
        while current is not None:
            next_temp = current.next
            current.next = previous
            previous = current
            current = next_temp
        return previous     