from jinja_main_handler import Handler


class MainPage(Handler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        visits = self.request.cookies.get('visits', '0')

        # make sure visits is an int
        if visits.isdigit():
            visits = int(visits) + 1
        else:
            visits = 0

        self.response.headers.add_header('Set-Cookie', 'visits={}'.format(visits))

        self.write("You've been here {} times!".format(visits))
