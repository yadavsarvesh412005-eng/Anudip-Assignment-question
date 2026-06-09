def revrse(self):
    prev=None
    curr = self.hrad # curr=10,20
    

    while curr: #10-<20->30-<40->50->None
        next=curr.next #next=20,30,40
        curr.next=prev #curr-next=None,10,20
        prev= curr #prev=10,20,30
        curr =next #curr=20,30,40
        self.head =prev 
#FIND MIDDLE Class
def middle(self):
    slow=self.head
    fast=self.head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next

        if slow== fast:
            return True
        return False

    
