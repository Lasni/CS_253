import webapp2
import jinja2
import os
from google.appengine.ext import db

# locate the folder where the templates are and assign it to a variable
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
# load said templates and store them in a variable
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                                       autoescape=True)


# NEED MORE INFO
def blog_key(name='default'):
    return db.Key.from_path('blog', name)


def render_str(template, **params):
    """ Global function for rendering a template with params.
        Needed for use inside the Post class that doesn't inherit from BlogHandler class.
    """
    t = jinja_environment.get_template(template)
    return t.render(params)


# def render_post(response, post):
#     response.out.write('<b>' + post.subject + '</b><br>')
#     response.out.write(post.content)


# Main BlogHandler class with methods for rendering the templates with params
class BlogHandler(webapp2.RequestHandler):
    def write(self, *args, **kwargs):
        self.response.out.write(*args, **kwargs)

    @staticmethod
    def render_str(template, **params):
        return render_str(template, **params)

    def render(self, template, **kwargs):
        self.write(self.render_str(template, **kwargs))


# Post class that stores data queried from the database
class Post(db.Model):
    subject = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)

    # render method that uses the above defined global render_str function
    def render(self):
        # each time that we render the template with params, we also replace all the newlines in the content with <br>
        self.rerender_text = self.content.replace('\n', '<br>')
        return render_str('post.html', p=self)


class BlogFront(BlogHandler):
    def get(self):
        posts = db.GqlQuery('SELECT * FROM Post ORDER BY created DESC LIMIT 10')
        self.render('front.html', posts=posts)


class PostPage(BlogHandler):
    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)

        if not post:
            self.error(404)
            return

        self.render('permalink.html', post=post)


class NewPost(BlogHandler):
    def get(self):
        self.render('newpost.html')

    def post(self):
        subject = self.request.get('subject')
        content = self.request.get('content')

        if subject and content:
            p = Post(parent=blog_key(), subject=subject, content=content)
            p.put()
            self.redirect('/blog/%s' % str(p.key().id()))
        else:
            error = "Enter the subject and content, please!"
            self.render('newpost.html', subject=subject,
                        content=content, error=error)
