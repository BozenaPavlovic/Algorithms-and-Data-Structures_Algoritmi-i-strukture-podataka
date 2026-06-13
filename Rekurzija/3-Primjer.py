def hello_world(n):
    for i in range(n):
        print("Hello, World!")

def hello_world_recursive(n):
    if n > 0:
        print("Hello, World!")
        hello_world_recursive(n - 1)
