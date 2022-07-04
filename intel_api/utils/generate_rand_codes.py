import random


def generate_rand_pin(length):
    return ''.join(random.sample('0123456789', length))