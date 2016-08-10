import webapp2
from lesson_2.quizzes.html_escaping import escape_html
from lesson_2.quizzes.valid_day import valid_day
from lesson_2.quizzes.valid_year import valid_year
from lesson_2.quizzes.valid_month import valid_month

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


class ValidateDates(webapp2.RequestHandler):

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