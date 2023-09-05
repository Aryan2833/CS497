class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeFromEnd(head, n):
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    if length == n:
        return head.next
    target_index = length - n
    current = head
    for _ in range(target_index - 1):
        current = current.next
    current.next = current.next.next

    return head
