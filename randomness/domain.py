# from random import random
import random

class RandomGenerator:

    def random(self):
        return random.random()


class Bingo:

    def __init__(self, random_generator: RandomGenerator):
        self.random_generator = random_generator

    def generate(self):
        return self.random_generator.random()
