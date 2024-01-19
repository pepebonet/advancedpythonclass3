"""
Script to write sum and subtract functions
"""
import time

# def example_decorator(func):
#     """
#     Example decorator
#     """
#     def wrapper(*args, **kwargs):
#         print('Hello')
#         result = func(*args, **kwargs)
#         print('Done')
#         print('World')
#         return result

#     return wrapper


def time_decorator(func):
    """
    Example decorator
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        time.sleep(1)
        result = func(*args, **kwargs)
        print(f'The code took: {time.time() - start} seconds')
        return result

    return wrapper


# @example_decorator
@time_decorator
def sum_two_nums(x, y):
    """
    Sum two numbers
    """

    return x + y

@time_decorator
def sub_two_nums(x, y):
    """
    Subtract two numbers
    """

    return x - y


if __name__ == "__main__":
    print(sum_two_nums(2, 3))
    print(sub_two_nums(2, 3))
    # pass
