class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        current = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        return dummy.next

# Helper function to create a linked list from a list
def create_linked_list(lst):
    head = None
    for value in reversed(lst):
        head = ListNode(value, head)
    return head

# Helper function to convert linked list to Python list
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Example usage:
if __name__ == "__main__":
    list1 = create_linked_list([1,2,4])
    list2 = create_linked_list([1,3,4])
    merged_head = Solution().mergeTwoLists(list1, list2)
    print(linked_list_to_list(merged_head))  # Output: [1, 1, 2, 3, 4, 4]