import random

def get_sample(min_, max_, cantidad):
    return [random.randint(min_, max_) for i in range(cantidad)]