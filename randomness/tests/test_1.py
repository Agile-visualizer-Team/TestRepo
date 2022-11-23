from unittest import mock

import pytest
from pytest_mock import mocker, MockFixture
import randomness.domain
from .. import RandomGenerator, Bingo


class RandomGeneratorFake(RandomGenerator):

    def __init__(self, times_before, number):
        self.times_before = times_before
        self.number = number

    def random(self):
        if self.times_before > 0:
            self.times_before -= 1
            return self.number + 1
        return self.number


class TestBingo:

    def test_find_number_random_stub_with_patch_mocker(self, mocker):
        mocker.patch.object(randomness.domain.random, 'random', return_value=1)
        bingo = Bingo(RandomGenerator())
        for i in range(10):
            # print(bingo.generate())
            assert bingo.generate() != 2

    def test_find_number_random_stub_with_patch_unittest(self):
        with mock.patch.object(RandomGenerator, 'random', return_value=3):
            bingo = Bingo(RandomGenerator())
            for i in range(10):
                assert bingo.generate() != 2

    def test_find_number_random_stub_with_mock(self, mocker):
        random_generator = mocker.Mock(spec=RandomGenerator())
        random_generator.random = lambda: 10
        bingo = Bingo(random_generator)
        for i in range(10):
            assert bingo.generate() != 2

    def test_find_number_random_fake(self):
        times_before = 10
        number = 2
        random_generator = RandomGeneratorFake(times_before, number)
        bingo = Bingo(random_generator)
        for i in range(times_before):
            assert bingo.generate() != number
        assert bingo.generate() == number
