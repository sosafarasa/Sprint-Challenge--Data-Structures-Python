
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            #go left
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            #go right
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        
        if target < self.value:
            #go left
            if not self.left:
                #not here
                return False
            else:
                return self.left.contains(target)
        else:
            # Target >= slef.value
            if not self.right:
                return False
            else:
                return self.right.contains(target)