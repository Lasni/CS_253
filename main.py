# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2


class MainPage(webapp2.RequestHandler):
    def get(self):
        # self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(form)

    def post(self):
        user_day = DateValidation.valid_day(self.request.get('day'))
        user_month = DateValidation.valid_month(self.request.get('month'))
        user_year = DateValidation.valid_year(self.request.get('year'))

        if not (user_day and user_month and user_year):
            self.response.out.write(form)
        else:
            self.response.out.write("Thanks! That's a totally valid date.")


# class TestHandler(webapp2.RequestHandler):
#     def post(self):
#         # q = self.request.get('q')
#         # self.response.out.write(q)
#         self.response.headers['Content-Type'] = 'text/plain'
#         self.response.out.write(self.request)


class DateValidation:
    def __init__(self):
        pass

    def valid_year(year):
        if year.isdigit():
            year = int(year)
            if 1900 <= year <= 2020:
                return year
        return None

    def valid_month(month):
        month_abv = dict((m[:3].lower(), m) for m in months)
        if month:
            short_month = month[:3].lower()
            return month_abv.get(short_month)

    def valid_day(day):
        if day.isdigit():
            day = int(day)
            if 1 <= day <= 31:
                return day
        return None


app = webapp2.WSGIApplication([
    ('/', MainPage), ], debug=True)

form = """
<form>
	<label>
		Day
		<input type="text" name="day">
	</label>
		Month
		<input type="text" name="month">
	</label>
	<label>
		Year
		<input type="text" name="year">
	</label>
	<br>
	<br>
	<input type="submit">
</form>
"""

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
