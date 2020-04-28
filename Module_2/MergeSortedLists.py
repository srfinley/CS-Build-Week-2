# https://leetcode.com/problems/merge-two-sorted-lists/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # handle empty input
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        # set up head (needed for return)
        if l1.val < l2.val:
            head = ListNode(l1.val)
            l1 = l1.next
        else:
            head = ListNode(l2.val)
            l2 = l2.next

        # handle lists of length 1
        if l1 is None:
            head.next = l2
        elif l2 is None:
            head.next = l1

        # set up "current" for loop
        elif l1.val < l2.val:
            current = ListNode(l1.val)
            head.next = current
            l1 = l1.next
        else:
            current = ListNode(l2.val)
            head.next = current
            l2 = l2.next

        # loop until one list is emptied
        while l1 is not None and l2 is not None:
            if l1.val > l2.val:
                new_node = ListNode(l2.val)
                current.next = new_node
                current = new_node
                l2 = l2.next
            else:
                new_node = ListNode(l1.val)
                current.next = new_node
                current = new_node
                l1 = l1.next

        # in a try because current is only defined coniditonally
        try:
            if l1 is None:
                current.next = l2
            else:
                current.next = l1
        except:
            pass
        return head
        