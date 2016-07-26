import webapp2


class UserSignup(webapp2.RequestHandler):

    form = """
    <form method="post">
        <label>Name
        <input type="text" name="name" value="%(name)s">
        </label>
        <br>

    </form>
    """

    def write_form(self, name=""):
        self.response.out.write(self.form % {'name': name})

    def get(self):
        self.write_form()

    def post(self):
        name = self.request.get('name')
        self.write_form(name)
