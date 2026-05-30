# U svakom čvoru zamijeniti vrijednost sa Fibonacci brojem na poziciji originalne vrijednosti 
# (ako je key=5, postaje fib(5)=5)

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

def update_fibonacci(node):
    if node is None:
        return
    
    original_key = node.key
    
    update_fibonacci(node.left)
    update_fibonacci(node.right)
    
    node.key = fib(original_key)
