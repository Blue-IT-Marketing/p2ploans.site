import os
import webapp2
import jinja2
from google.appengine.ext import ndb
from google.appengine.api import users
from google.appengine.api import mail
import datetime,random,string
from google.appengine.api import memcache

import logging
#Jinja Loader
template_env = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.getcwd()))


class bgDataHandler(webapp2.RequestHandler):
    def get(self):
        pass



app = webapp2.WSGIApplication([
    ('/bg/data', bgDataHandler),

], debug=True)

