# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    @staticmethod
    def listnode_to_list(node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result
    @staticmethod
    def list_to_listnode(lst):
        dummy = ListNode()
        curr = dummy
        for val in lst:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next
    def mergeTwoLists(self, list1, list2):
        ls1 = Solution.listnode_to_list(list1)
        ls2 = Solution.listnode_to_list(list2)
        res = []
        i = 0
        j = 0
        while i < len(ls1) and j < len(ls2):
            if ls1[i] < ls2[j]:
                res.append(ls1[i])
                i += 1
            else:
                res.append(ls2[j])
                j += 1

        while i < len(ls1):
            res.append(ls1[i])
            i += 1

        while j < len(ls2):
            res.append(ls2[j])
            j += 1
        return self.list_to_listnode(res)
