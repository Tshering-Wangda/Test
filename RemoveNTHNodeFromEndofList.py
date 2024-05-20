# Definitionforsingly-linkedlist. 
# class ListNode(object): 
#   def__init__(self,val=0,next=None): 
#       self.val=val 
#       self.next=next 
class Solution(object): 
    def removeNthFromEnd(self, head, n): 
        # Initialize a dummy node with value 0 and point its next to the head of the original list. 
        dummy = ListNode(0,head) 
        
        # Initialize two pointers 'slow' and 'fast' to the dummy node. 
        # Both pointers will be used to find the node to be removed. 
        slow = fast = dummy
        
        # Move the 'fast' pointer n steps ahead of the 'slow' pointer. 
        for i in range(n): 
            fast = fast.next  
            
            # Move both 'slow' and 'fast' pointers until 'fast' reaches the last node. 
            # At this point, 'slow' will be pointing to the node before the one to be removed. 
            while fast.next: 
                slow = slow.next 
                fast = fast.next
                
                # Remove the Nth node from the end by updating 'slow.next' to skip the next node.
                slow.next = slow.next.next 
                # Return the head of the modified list (next node after the dummy node). 
                return dummy.next