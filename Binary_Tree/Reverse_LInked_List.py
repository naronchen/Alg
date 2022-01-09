class Solution:
    
    def reverseLinkedList(self, head, k):
        
        new_head, ptr = None, head
        while k:

            next_node = ptr.next

            ptr.next = new_head
            new_head = ptr
            
            # Move on to the next node
            ptr = next_node
            
            # Decrement the count of nodes to be reversed by 1
            k -= 1
        
        # Return the head of the reversed list
        return new_head
                
    
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        
        count = 0
        ptr = head
        
        # First, see if there are atleast k nodes
        # left in the linked list.
        while count < k and ptr:
            ptr = ptr.next
            count += 1
        
        # If we have k nodes, then we reverse them
        if count == k: 
            
            # Reverse the first k nodes of the list and
            # get the reversed list's head.
            reversedHead = self.reverseLinkedList(head, k)
            
            # Now recurse on the remaining linked list. Since
            # our recursion returns the head of the overall processed
            # list, we use that and the "original" head of the "k" nodes
            # to re-wire the connections.
            head.next = self.reverseKGroup(ptr, k)
            return reversedHead
        return head
