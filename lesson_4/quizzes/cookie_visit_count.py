from jinja_main_handler import Handler
import hmac

# secret string for hmac
SECRET = "imsosecret"


def hash_str(s):
    return hmac.new(SECRET, s).hexdigest()


def make_secure_val(s):
    return "{}|{}".format(s, hash_str(s))


def check_secure_val(s):
    val, hashed_val = s.split("|")
    if hash_str(val) == hashed_val:
        return val


class MainPage(Handler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'

        # set number of visits to 0 by default
        visits = 0
        # visit_cookie_str is in the format of "visits|hash"
        visit_cookie_str = self.request.cookies.get('visits')

        if visit_cookie_str:
            cookie_val = check_secure_val(visit_cookie_str)
            if cookie_val:
                visits = int(cookie_val)
        visits += 1

        new_cookie_val = make_secure_val(str(visits))

        # # make sure visits is an int
        # if visits.isdigit():
        #     visits = int(visits) + 1
        # else:
        #     visits = 0

        self.response.headers.add_header('Set-Cookie', 'visits={}'.format(new_cookie_val))

        self.write("You've been here {} times!".format(visits))
