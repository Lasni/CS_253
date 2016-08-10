from jinja_main_handler import *
from google.appengine.ext import db


class Art(db.Model):
    title = db.StringProperty(required=True)
    art = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)


class AsciiHandler(Handler):

    def get(self):
        self.render_front()

    def post(self):
        title = self.request.get('title')
        art = self.request.get('art')

        if art and title:
            a = Art(title=title, art=art)
            a.put()
            self.redirect('/ascii-art')
        else:
            error = "Need both the title and the art."
            self.render_front(title, art, error)

    def render_front(self, title="", art="", error=""):
        arts = db.GqlQuery("SELECT * FROM Art ORDER BY created DESC")
        self.render('front.html', title=title, art=art, error=error, arts=arts)




