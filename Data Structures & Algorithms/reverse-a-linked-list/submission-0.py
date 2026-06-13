class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        new_head = self.reverseList(head.next)
        head.next.next = head   # reverse the link
        head.next = None        # cut the old forward link
        return new_head