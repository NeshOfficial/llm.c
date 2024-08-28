import requests
from functools import wraps

def exception_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"An error occurred in {func.__name__}: {e}")
            return None
    return wrapper

@exception_handler
def fetch_data_from_api(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

def square_numbers(numbers):
    return [num ** 2 for num in numbers]

@exception_handler
def save_data_to_file(data, filename):
    with open(filename, 'w') as file:
        for item in data:
            file.write(f"{item}\n")
    print(f"Data saved to {filename}")


