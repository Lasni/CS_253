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

from lesson_2.html_escaping import escape_html
from lesson_2.valid_day import valid_day
from lesson_2.valid_month import valid_month
from lesson_2.valid_year import valid_year
from lesson_2 import rot_13


class MainPage(webapp2.RequestHandler):
    def write_form(self, error="", day="", month="", year=""):
        self.response.out.write(form % {"error": escape_html(error), "day": escape_html(day),
                                        "month": escape_html(month), "year": escape_html(year)})

    def get(self):
        self.write_form()

    def post(self):
        user_day = self.request.get('day')
        user_month = self.request.get('month')
        user_year = self.request.get('year')

        day = valid_day(user_day)
        month = valid_month(user_month)
        year = valid_year(user_year)

        if not (day and month and year):
            self.write_form("That doesn't look valid to me.",
                            user_day, user_month, user_year)
        else:
            self.redirect("/thanks")


class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("Thanks! That's a totally valid date.")


# class TestHandler(webapp2.RequestHandler):
#     def post(self):
#         # q = self.request.get('q')
#         # self.response.out.write(q)
#         self.response.headers['Content-Type'] = 'text/plain'
#         self.response.out.write(self.request)


app = webapp2.WSGIApplication([
    ('/', MainPage), ('/thanks', ThanksHandler), ('/rot13', rot_13.Rot13)], debug=True)

form = """
<form method="post">
    What's your birthday?
    <br>
    <br>
    <label>
        Day
        <input type="text" name="day" value="%(day)s">
    </label>
        Month
        <input type="text" name="month" value="%(month)s">
    </label>
    <label>
        Year
        <input type="text" name="year" value="%(year)s">
    </label>
    <div style="color: red">%(error)s</div>
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

month_abv = dict((m[:3].lower(), m) for m in months)
