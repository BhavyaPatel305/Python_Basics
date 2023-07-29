# program to filter leap years from a given list of years
years = [1999, 2000, 3004, 2009, 2004, 2008, 2012 ]

fl = list(filter(lambda x:(x % 4 == 0 and (x % 100 != 0 or x % 400 == 0)), years))
print(fl)