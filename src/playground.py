import unittest
import numpy as np

class MyPlayground(unittest.TestCase):

    def test_zip(self):
        list_a = [0, 1, 2]
        list_b = ['a', 'b', 'c']
        for x, y in zip(list_a, list_b):
            print(x, y)

    def test_np(self):
        print(np.random.randn(2, 3))
        # w: 3 lists with [neurals/activations of layer for each row, inputs cols]
        # b: 3 lists with [neurals/activations of layer for each row, 1]


