def make_multiplier(n):
    def multiplier(x):
        return x * n
    
    return multiplier


double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))
print(triple(5))

print(make_multiplier(5)(13))