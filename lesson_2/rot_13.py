import cgi
import webapp2


class Rot13(webapp2.RequestHandler):

    form = """
    <html>
      <head>
        <title>Unit 2 Rot 13</title>
      </head>

      <body>
        <h2>Enter some text to ROT13:</h2>
        <form method="post">
          <textarea name="text" style="height: 100px; width: 400px;">%(text)s</textarea>
          <br>
          <input type="submit" value="submit">
        </form>
      </body>
    </html>
    """

    def write_form(self, text=""):
        self.response.out.write(self.form % {"text": text})

    def get(self):
        self.write_form()

    def post(self):
        text = self.request.get("text")
        encoded_text = text.encode("rot13")
        self.write_form(cgi.escape(encoded_text, quote=True))