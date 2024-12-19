from itertools import cycle, count

b = [1, 2, 3, 4, 5]
a = range(5)

print("\n1. Iterablelardan:")
for item in b:
    print(f"Listdan: {item}")

for num in a:
    print(f"Rangedan: {num}")


class Counter:
    def __init__(self, past, balant):
        self.past = past
        self.balant = balant

    def __iter__(self):
        return self

    def __next__(self):
        if self.past > self.balant:
            raise StopIteration
        else:
            self.past += 1
            return self.past - 1

print("\n2. Iteratorlar:")
init = Counter(1, 5)
for num in init:
    print(f"Custom iterator: {num}")

ite = iter(b)
print(next(ite))
print(next(ite))

# 3. Generatorlar
# Oddiy generator funksiyasi
def my_generator():
    for i in range(3):
        yield i

print("\n3. Generatorlar:")
for value in my_generator():
    print(f"Generator funksiyasi: {value}")

# Generator ifodasi bilan
generator_expression = (x**2 for x in range(5))
for value in generator_expression:
    print(f"Generator ifodasi: {value}")

# 4. itertools moduli yordamida iterable va iteratorlar
print("\n4. itertools yordamida:")
cycled_colors = cycle(['red', 'blue', 'green'])
print(f"Cycle: {next(cycled_colors)}")
print(f"Cycle: {next(cycled_colors)}")
print(f"Cycle: {next(cycled_colors)}")

counter = count(start=1, step=2)
for _ in range(3):
    print(f"Count: {next(counter)}")
