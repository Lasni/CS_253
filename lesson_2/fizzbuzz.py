from jinja_main_handler import *


class FizzBuzzHandler(Handler):
    def get(self):
        # n = self.request.get('n', 0)
        # n = n and int(n)
        n = 100
        self.render('fizzbuzz.html', n=n)

