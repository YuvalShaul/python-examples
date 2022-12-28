
# v1 = 5

def outer():
    v1 = 6
    def inner():
        # choose and see the differences:
        global v1
        # nonlocal v1
        v1 = 7
        print(v1)
    inner()
    print("v1 outer:", v1)
    

outer()

print('v1 global:', v1)

