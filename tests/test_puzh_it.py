import unittest

import puzh


class PuzhTestCase(unittest.TestCase):

    def test_non_string_token(self):
        with self.assertRaises(TypeError):
            puzh.it('test', token=0)

    def test_none_token(self):
        with self.assertRaises(TypeError):
            puzh.it('test', token=None)

    def test_non_string_seperator(self):
        with self.assertRaises(TypeError):
            puzh.it('test', token='secret', sep=0)

    def test_non_bool_silent(self):
        with self.assertRaises(TypeError):
            puzh.it('test', token='secret', silent=0)
