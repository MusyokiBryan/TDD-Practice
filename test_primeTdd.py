import unittest
import prime

class PrimeTestCase(unittest.TestCase):
    def test_2_is_prime(self):
        results = prime.prime(2)
        self.assertTrue(results == [2])

    def test_0_is_not_prime(self):
        pass

    def test_reject_non_ints(self):
        pass

    def test_prime_30_list(self):
        results = prime.prime(30)
        self.assertListEqual(results, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])


if __name__ == '__main__':
    unittest.main() #running the test
