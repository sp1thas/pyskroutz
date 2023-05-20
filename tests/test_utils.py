import unittest
from argparse import Namespace

from pyskroutz.utils import rgetattr, rsetattr


class TestUtils(unittest.TestCase):
    """Test module utils"""

    def test_rgetattr_util(self):
        ns_obj = Namespace()
        ns_obj.a = Namespace()
        ns_obj.a.b = 1
        self.assertEqual(rgetattr(ns_obj, "a.b"), 1)

    def test_rsetattr_util(self):
        ns_obj = Namespace()
        ns_obj.a = Namespace()
        rsetattr(ns_obj, "a.b", 1)
        self.assertEqual(1, ns_obj.a.b)
