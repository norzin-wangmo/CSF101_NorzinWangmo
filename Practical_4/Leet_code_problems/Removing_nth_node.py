class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy
        for _ in range(n):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
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
    head = create_linked_list([1,2,3,4,5])
    new_head = Solution().removeNthFromEnd(head, 2)
    print(linked_list_to_list(new_head))  # Output: [1, 2, 3, 5]