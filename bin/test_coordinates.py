from unittest import TestCase
from bin.coordinates import *
import unittest


class TestCoordinates(TestCase):
    def setUp(self):
        self.coord = Corray(50, 12)
    def test_len(self):
        self.assertEqual(len(self.coord), 2)
    def test_lat(self):
        self.assertEqual(self.coord['lat'], 50)
    def test_lon(self):
        self.assertEqual(self.coord['lon'], 12)
    def test_set(self):
        self.coord['lat'] = 66
        self.coord['lon'] = 33
        self.assertEqual(self.coord['lat'], 66)
        self.assertEqual(self.coord['lon'], 33)


unittest.main()