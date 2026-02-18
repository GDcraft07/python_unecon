def make_multiplier(n):
    const = 52
    def multiplier(x):
        return const * x * n
    
    return multiplier


double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))
print(triple(5))

print(make_multiplier(5)(13))


def funk(n):
    return n

lst = [1, 2, 3]

res = funk(lst)
print(lst)

lst[0] = 0
print(lst)