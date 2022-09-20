class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        # remember how many slots we have
        # non-null nodes occupy one slot but creates two new slots
        # null nodes occupy one slot
        
        p = preorder.split(',')
        
        # initially we have one empty slot to put the root in it
        slot = 1
        
        for node in p:
            
            # no empty slow to put the current node
            if slot == 0:
                return False
            
            # a null node?
            if node == '#':
                # occupy slot
                slot -= 1
            else:
                # create new slot
                slot += 1
        
        # we don't allow empty slots at the end
        return slot == 0
        