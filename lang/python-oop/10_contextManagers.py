import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self
    
    def __exit__(self, exc_type, exc, tb):
        self.end = time.time()
        print(f"elapse time {self.end - self.start}")



if __name__ == "__main__":
    with Timer():
        count = 0
        for i in range(1_000_000):
            count += 1
        print(count)