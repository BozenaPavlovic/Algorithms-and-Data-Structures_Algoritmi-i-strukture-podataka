def traverse(tree, traversaltype='in'):
    # tree je korijen stabla koje se predaje
    result = []
    def obilazak(cvor):
        if cvor is None: return
        if traversaltype == 'pre': result.append(cvor.key)
        obilazak(cvor.left)
        if traversaltype == 'in': result.append(cvor.key)
        obilazak(cvor.right)
        if traversaltype == 'post': result.append(cvor.key)
    obilazak(tree)
    return result
