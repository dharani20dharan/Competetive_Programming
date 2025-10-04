# Leet code 160: Intersection of Two Linked Lists

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type headA, headB: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        pA, pB = headA, headB

        # Traverse until they meet or both become None
        while pA != pB:
            # If pointer reaches end, switch to other list’s head
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA

        # Either intersection node or None
        return pA
