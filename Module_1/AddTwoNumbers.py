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
        # SECOND SOLUTION UNFINISHED:
        # vals = []
        # carry = 0
        # while l1 is not None and l2 is not None:
        #     new_val = l1.val + l2.val
        #     vals.append((new_val + carry) % 10)
        #     carry = (new_val + carry) // 10
        #     l1 = l1.next
        #     l2 = l2.next
        # deal with one input being longer
        # then convert vals to the ll
