import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def mergeKLists(lists):
    temp = ListNode()
    current = temp

    min_heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(min_heap, (node.val, i))

    while min_heap:
        val, i = heapq.heappop(min_heap)
        current.next = ListNode(val)
        current = current.next
        if lists[i].next:
            lists[i] = lists[i].next
            heapq.heappush(min_heap, (lists[i].val, i))

    return temp.next
