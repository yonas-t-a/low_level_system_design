def count_to(max):
    current = 0
    while current < max:
        current += 1
        yield current


def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a+b
        count += 1
        
        

if __name__ == "__main__":
    for number in count_to(5):
        print(number)
    print("=======")
    for num in fibonacci(10):
        print(num)
