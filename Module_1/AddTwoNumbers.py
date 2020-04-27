# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def list_to_num(self, ll):
        """Converts a linked list to an int"""
        power = 0
        node = ll
        total = 0

        while node is not None:
            total += node.val * (10 ** power)

            power += 1
            node = node.next
            
        return total
    
    def num_to_list(self, num):
        """Converts an int to a linked list"""
        nodes = [ListNode(int(digit)) for digit in str(num)]
        
        for index, node in enumerate(nodes[1:]):
            node.next = nodes[index]
            
        return nodes[-1]
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        value = self.list_to_num(l1) + self.list_to_num(l2)
        return self.num_to_list(value)
        # SECOND SOLUTION FINISHED:
        # basically the same stats as the first one
        # nodes = []
        # carry = 0

        # # add each corresponding digit, or zero when one number is longer
        # while l1 is not None or l2 is not None:
        #     try:
        #         val1 = l1.val
        #     except AttributeError:
        #         val1 = 0
        #     try:
        #         val2 = l2.val
        #     except AttributeError:
        #         val2 = 0
        #     new_val = val1 + val2 + carry
        #     nodes.append(ListNode(new_val % 10))
        #     carry = new_val // 10
        #     try:
        #         l1 = l1.next
        #     except AttributeError:
        #         l1 = None
        #     try:
        #         l2 = l2.next
        #     except AttributeError:
        #         l2 = None
        # if carry:
        #     nodes.append(ListNode(carry))
        # for index, node in enumerate(nodes[:-1]):
        #     node.next = nodes[index+1]
        # return nodes[0]
