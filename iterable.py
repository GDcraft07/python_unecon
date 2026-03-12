# s = "mother dishes ramy"

# for i in s:
#     print(i)


# print(sum([i for i in range(5)]))

# print(sum(i for i in range(5)))

# print(sum(range(5)))

# a = [1, 2, 3]

# my_iter = iter(a)

# print(next(my_iter))


def count_gen():
    counter = 1

    while True:
        yield counter
        counter += 1


my_gen = iter(count_gen())

print(next(my_gen))