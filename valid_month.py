# -----------
# User Instructions
#
# Modify the valid_month() function to verify
# whether the data a user enters is a valid
# month. If the passed in parameter 'month'
# is not a valid month, return None.
# If 'month' is a valid month, then return
# the name of the month with the first letter
# capitalized.
#

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']


def valid_month(month):
    if month.capitalize() in months:
        return month.capitalize()
    return None


print valid_month("january")
# => "January"
print valid_month("January")
# => "January"
print valid_month("foo")
# => None
print valid_month("")
# => None
