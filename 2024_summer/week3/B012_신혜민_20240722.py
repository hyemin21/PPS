def post_order(preorder):
    if not preorder:
        return
    root = preorder[0]
    idx = len(preorder)
    for i in range(1, len(preorder)):
        if preorder[i] > root:
            idx = i
            break
    post_order(preorder[1:idx])
    post_order(preorder[idx:])
    print(root)

preorder = list(map(int, input().split()))
post_order(preorder)
