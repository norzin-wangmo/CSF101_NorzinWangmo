class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev = None
    current = head
    
    while current is not None:
        next_temp = current.next  # Store next node
        current.next = prev       # Reverse the link
        prev = current            # Move prev one step
        current = next_temp       # Move current one step
    
    return prev  # prev is the new head of the reversed list

# Helper function to print the linked list
def printList(head):
    current = head
    elements = []
    while current:
        elements.append(str(current.val))
        current = current.next
    print(" -> ".join(elements))

# Example usage:
# Create linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print("Original list:")
printList(head)

reversed_head = reverseList(head)
print("Reversed list:")
printList(reversed_head)
