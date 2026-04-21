import random
def count_numbers():
    numbers = [random.randint(1, 100) for __ in range(10)]
    print("List:", numbers)
    count = sum(1 for num in numbers if num % 3 == 0 and num % 5 != 0)
    return count
result = count_numbers()
print(result)
