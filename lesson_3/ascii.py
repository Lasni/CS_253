from jinja_main_handler import *


class AsciiHandler(Handler):
    def get(self):
        self.render('front.html')

