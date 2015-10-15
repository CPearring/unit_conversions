#!/usr/bin/env python

#Command line script to convert a single number to and from several units because shits and giggles

#I didn't put spaces between the # and the first letter to show that I didn't copy it loolololo

import argparse

from src.convert import kilometers_to_miles, miles_to_kilometers,\
	years_to_minutes, minutes_to_years, migranes_to_heart_attacks


#Parse command line args
parser = argparse.ArgumentParser()
parser.add_argument('value', type=float, help="The number to be converted")
args = parser.parse_args()

#Perform conversions
#km to miles
to_miles = kilometers_to_miles(args.value)
print("{0} kilometers is {1} miles".format(args.value, to_miles))

#miles to km
to_km = miles_to_kilometers(args.value)
print("{0} miles is {1} kilometers".format(args.value, to_km))

#years to minutes
to_minutes = years_to_minutes(args.value)
print("{0} years is {1} minutes".format(args.value, to_minutes))

#minutes to years
to_years = minutes_to_years(args.value)
print("{0} minutes is {1} years".format(args.value, to_years))

#migranes to heart_attacks (compeltely made up lolz)
to_heart_attacks = migranes_to_heart_attacks(args.value)
print("{0} migranes is {1} heart attacks".format(args.value, to_heart_attacks))
