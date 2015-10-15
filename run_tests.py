#!/usr/bin/env python

import unittest

from src.convert import kilometers_to_miles, miles_to_kilometers,\
	years_to_minutes, minutes_to_years, migranes_to_heart_attacks

class TestConvert(unittest.TestCase):

	def test_km_to_miles(self):
		actual = kilometers_to_miles(1)
		expected = 0.621
		self.assertAlmostEqual(actual, expected, delta=0.01)

	def test_miles_to_km(self):
		actual = miles_to_kilometers(1)
		expected = 1.609
		self.assertAlmostEqual(actual, expected, delta=0.01)

	def test_years_to_minutes(self):
		#Google says blah
		self.assertEqual(525600, years_to_minutes(1))

	def test_minutes_to_years(self):
		self.assertEqual(1, minutes_to_years(525600))

	def test_migranes_to_heart_attacks(self):
		actual = migranes_to_heart_attacks(1)
		expected = 85
		self.assertEqual(actual, expected)

#################

if __name__ == '__main__':
	unittest.main()
