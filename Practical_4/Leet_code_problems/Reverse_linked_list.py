class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        prev = None
        current = head
        while current is not None:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        return prev

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
    reversed_head = Solution().reverseList(head)
    print(linked_list_to_list(reversed_head))  # Output: [5, 4, 3, 2, 1]