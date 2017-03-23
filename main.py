#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
#
import webapp2
import random

def getRandomFortune():
    fortunes=[
        "I see much code in your future",
        "Consider eating more fortune cookies",
        "You have tamed the mighty Python, now must free it on the web!"
        ]
    index =random.randint(0,2)
    return fortunes[index]

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header="<h1>Fortune Cookie</h1>"
        fortune= "<strong>"+getRandomFortune()+"</strong>"
        fortune_sentence="Your Fortune: " + fortune
        fortune_para= "<p>"+fortune_sentence+"</p>"

        num= "<strong>"+str(random.randint(0,100))+"</strong>"
        number_sentence= "Your lucky number: " +num
        number_para="<p>"+number_sentence+"</p>"

        another_cookie="<a href='.'><button>Anothr Cookie Pls!</button></a>"

        content=header + fortune_para + number_para+another_cookie
        self.response.write(content)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
