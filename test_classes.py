from unittest import TestCase
from weather import *
from airports import *
from aircrafts import *
from delay import *
import unittest

class TestWeather(TestCase):
    def setUp(self):
        print("..Weather test...")
        self.a = Weather()

    def test_weather_coord(self):
        b = self.a.weather_coord_forecast(Corray(50.40, 30.45), '2019-05-14')
        self.assertIn(b, self.a.dat)
        b = self.a.weather_coord(Corray(50.40, 30.45))
        self.assertIn(b, self.a.dat)

    def test_danger(self):
        self.a.weather_coord_forecast(Corray(50.40, 30.45), '2019-05-14')
        b = self.a.danger()
        self.assertEqual(0 <= b <= 5/50, True)

class TestAirport(TestCase):
    def setUp(self):
        print("..Airport test...")
        self.net = AirportsNet()

    def test_searchers(self):
        b = self.net.find_by_airname("Katowice International Airport")
        self.assertEqual(b, Airport("Katowice International Airport", "Poland", "Katowice", "KTW", "EPKT", "50.4743", "19.08"))

class TestAircraft(TestCase):
    def setUp(self):
        print("..Aircraft test...")
        self.net = AircraftsNet()

    def test_searchers(self):
        c = self.net.search_year(self.net.craft_dat[7].name)
        self.assertEqual(c, 2013)

    def test_delay_extender(self):
        c = self.net.delay_extender(5, "B748")
        self.assertEqual(c, 5.009)

class TestDelay(TestCase):
    def setUp(self):
        print("..Delay test...")
        self.b = Delay("FRA")

    def test_delay(self):
        a = self.b.alter_del()
        self.assertEqual(type(a), float)
        self.assertLessEqual(a, 1)


unittest.main()