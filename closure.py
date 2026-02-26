# def make_multiplier(n):
#     const = 52
#     def multiplier(x):
#         return const * x * n
    
#     return multiplier


# double = make_multiplier(2)
# triple = make_multiplier(3)

# print(double(5))
# print(triple(5))

# print(make_multiplier(5)(13))

# # nonlocal

def count_calls():
    counter = 0

    def closure(print_result=False):
        nonlocal counter

        if print_result:
            return counter
        
        counter += 1
        
        return counter
    
    return closure


counter = count_calls()

for _ in range(5):
    counter()


print(counter(True))
print(counter())