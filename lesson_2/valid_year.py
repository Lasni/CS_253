# -----------
# User Instructions
#
# Modify the valid_year() function to verify
# whether the string a user enters is a valid
# year. If the passed in parameter 'year'
# is not a valid year, return None.
# If 'year' is a valid year, then return
# the year as a number. Assume a year
# is valid if it is a number between 1900 and
# 2020.
#


def valid_year(year):
    if year.isdigit():
        year = int(year)
        if 1900 <= year <= 2020:
            return year
    return None


print valid_year('0')
# => None
print valid_year('-11')
# => None
print valid_year('1950')
# => 1950
print valid_year('2000')
# => 2000
