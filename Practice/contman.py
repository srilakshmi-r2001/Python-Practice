import time

class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.time()
        elapsed_time = self.end_time - self.start_time
        print(f"Time elapsed: {elapsed_time} seconds")

# Using the custom context manager
with Timer():
    # Code block whose execution time we want to measure
    time.sleep(1)