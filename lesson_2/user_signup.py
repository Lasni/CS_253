import webapp2
import re

signup_form = """
<!DOCTYPE html>

<html>
    <head>
        <title>Signup Form</title>
    </head>

    <body>
        <h2>Signup</h2>
        <form method="post">
            <label>Username
                <input type="text" name="username" value="%(username)s">
                <span style="color: red">%(usr_err)s</span>
            </label>
            <br>
            <label>Password
                <input type="password" name="password" value="%(password)s">
                <span style="color: red">%(pass_err)s</span>
            </label>
            <br>
            <label>Verify Password
                <input type="password" name="verify_pass" value="%(verify_pass)s">
                <span style="color: red">%(ver_err)s</span>
            </label>
            <br>
            <label>Email (optional)
                <input type="email" name="email" value="%(email)s">
                <span style="color: red">%(email_err)s</span>
            </label>
            <br>
            <input type="submit" name="submit">
        </form>
    </body>
    """

welcome_form = """
    <!DOCTYPE html>

    <html>
        <head>
            <title>Unit 2 Welcome</title>
        </head>

        <body>
            <h2>Welcome, %(username)s!</h2>
        </body>
    </html>
"""


def valid_username(username):
    USER_RE = re.compile("^[a-zA-Z0-9_-]{3,20}$")
    return username and USER_RE.match(username)


def valid_password(password):
    PASS_RE = re.compile("^.{3,20}$")
    return password and PASS_RE.match(password)


def valid_email(email):
    EMAIL_RE = re.compile("^[\S]+@[\S]+.[\S]+$")
    return email and EMAIL_RE.match(email)


class UserSignup(webapp2.RequestHandler):
    def write_form(self, username="", password="", verify_pass="", email="",
                   usr_err="", pass_err="", ver_err="", email_err=""):
        self.response.out.write(signup_form % {'username': username,
                                               'password': password,
                                               'verify_pass': verify_pass,
                                               'email': email,
                                               'usr_err': usr_err,
                                               'pass_err': pass_err,
                                               'ver_err': ver_err,
                                               'email_err': email_err})

    def get(self):
        self.write_form()

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        verify_pass = self.request.get('verify_pass')
        email = self.request.get('email')
        usr_err = ""
        pass_err = ""
        ver_err = ""
        email_err = ""
        usr_bool = True
        pass_bool = True
        email_bool = True

        if not valid_username(username):
            usr_err = "That's not a valid username."
            usr_bool = False
        if not valid_password(password):
            pass_err = "That's not a valid password."
            pass_bool = False
        elif password != verify_pass:
            ver_err = "Your passwords didn't match."
        if not valid_email(email):
            email_err = "That's not a valid email."
            email_bool = False

        if usr_bool and pass_bool and email_bool and (password == verify_pass):
            self.redirect('/welcome?username=' + username)
        else:
            self.write_form(username, password, verify_pass, email,
                            usr_err, pass_err, ver_err, email_err)


class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        username = self.request.get('username')
        if valid_username(username):
            self.response.out.write(welcome_form % {'username': username})
        else:
            self.redirect('/')
