
def is_prime(number):
    """Return True id numbeer is prime."""
    for element in range(2,number):
        if number % element == 0:
            return False
        return True


def print_next_prime(number):
    """Print the closest prime number larger than numbers"""
    index = number
    while True:
        index +=1
        if is_prime(index):
            print(index)
