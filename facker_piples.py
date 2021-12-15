import time


def test_time(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        res = func(*args, **kwargs)
        et = time.time()
        dt = et - st
        print(f"times = {dt}")
        return res

    return wrapper


@test_time
def get_nod(a , b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


@test_time
def get_fast_nod(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

# get_nod = test_time(get_nod)
# get_fast_nod = test_time(get_fast_nod)
res2 = get_fast_nod(2, 1000000)
res = get_nod(2, 1000000)

print( res2)
