def maxValPath(root):
    if root is None: return -999999999 # if it is null, you would just choose the other path
    if root.left is None and root.right is None: return [root.val]

    left = maxValPath(root.left)
    right = maxValPath(root.right)

    if sum(left)> sum(right): return [root.val] + left
    else: return [root.val] + right

