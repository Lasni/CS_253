import webapp2
import jinja2
import os
from google.appengine.ext import db


template_dir = os.path.join(os.path.dirname(__file__), 'blog_2_templates')
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                                       autoescape=True)


def render_str(template, **params):
    t = jinja_environment.get_template(template)
    return t.render(params)


class BlogPost(db.Model):
    subject = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)

    def render(self):
        self.format_content = self.content.replace('\n', '<br>')
        return render_str('post.html', p=self)



# class BasicHandler(webapp2.RequestHandler):
#     def write_html(self, template_file, **kwargs):
#         template = jinja_environment.get_template(template_file)
#         self.response.out.write(template.render(**kwargs))

class BlogHandler(webapp2.RequestHandler):
    def write(self, *args, **kwargs):
        self.response.out.write(*args, **kwargs)

    def render_str(self, template, **params):
        return render_str(template, **params)

    def render(self, template, **kwargs):
        self.write(self.render_str(template, **kwargs))


class BlogFront(BlogHandler):
    def get(self):
        posts = db.GqlQuery('SELECT * FROM BlogPost ORDER BY created DESC LIMIT 10')
        self.render('front.html', posts=posts)


class PostPage(BlogHandler):
    def get(self, post_id):
        post = BlogPost.get_by_id(int(post_id))

        if not post:
            self.error(404)
            return
        else:
            self.render('permalink.html', post=post)


class NewPost(BlogHandler):
    def get(self):
        self.render('newpost.html')

    def post(self):
        subject = self.request.get('subject')
        content = self.request.get('content')
        if not (subject and content):
            error_msg = "Enter subject and content."
            self.render('newpost.html', error=error_msg)
        else:
            p = BlogPost(subject=subject, content=content)
            p.put()
            x = str(p.key().id())
            self.redirect('/blog-2/{}'.format(x))
