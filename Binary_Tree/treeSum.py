def treeMin(root):
    if root is None: return None
    leftMin = treeMin(root.left)
    rightMin = treeMin(root.right)
    return min(root.val, leftMin, rightMin)

def DFStreeMin(root):
    if root is None: return None
    min = 99999999999999
    stack = [root]
    while len(stack) > 0 :
        current = stack.pop()
        if root.left is not None: stack.append(root.left)
        if root.right is not None: stack.append(root.right)
        if current < min:
            min = current
    
    return min

