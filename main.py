# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2


from lesson_2 import rot_13
from lesson_2 import date_validation
from lesson_2 import user_signup


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"] = "text/html"
        self.response.write(form)

    def post(self):
        val_date = self.request.get('date-val')
        rot13 = self.request.get('rot13')
        signup = self.request.get('user-signup')
        if val_date:
            self.redirect('/date-val')
        elif rot13:
            self.redirect('/rot13')
        elif signup:
            self.redirect('/user-signup')


app = webapp2.WSGIApplication([
    ('/', MainPage), ('/date-val', date_validation.ValidateDates),
    ('/thanks', date_validation.ThanksHandler), ('/rot13', rot_13.Rot13),
    ('/user-signup', user_signup.UserSignup)], debug=True)

form = """
<form method="post">
    <input type="submit" name="date-val" value="date validation">
    <input type="submit" name="rot13" value="rot13">
    <input type="submit" name="user-signup" value="user signup">
</form>
"""


