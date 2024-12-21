from itertools import cycle, count

# 1. Iterable yaratish
my_list = [1, 2, 3, 4, 5]  # Oddiy ro'yxat
my_range = range(5)  # range() iterable obyekt

print("\n1. Iterablelar:")
for item in my_list:
    print(f"Listdan: {item}")

for num in my_range:
    print(f"Rangedan: {num}")

# 2. Iterator yaratish
class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

print("\n2. Iteratorlar:")
custom_iterator = Counter(1, 5)
for num in custom_iterator:
    print(f"Custom iterator: {num}")

my_list_iterator = iter(my_list)  # Ro'yxatni iteratorga aylantirish
print(next(my_list_iterator))  # 1
print(next(my_list_iterator))  # 2

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
