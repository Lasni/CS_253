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


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"] = "text/html"
        self.response.write(form)

app = webapp2.WSGIApplication([
    ('/', MainPage), ('/date-validation', date_validation.ValidateDates),
    ('/thanks', date_validation.ThanksHandler), ('/rot13', rot_13.Rot13)], debug=True)

form = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Main page</title>
    </head>
    <body>
        <button>Date validation</button> <button>ROT 13</button>
        <br>
        <button>three</button> <button>four</button>
    </body>
    </html>
"""


