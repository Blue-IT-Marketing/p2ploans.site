#!/usr/bin/env python

# Copyright 2007 Google Inc.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import os
import webapp2
import jinja2
from google.appengine.ext import ndb
from google.appengine.api import users
from Contact import Contact
from profiles import Profile
#Jinja Loader
import logging
template_env = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.getcwd()))



class MainHandler(webapp2.RequestHandler): # Loading the Main App Window
    def get(self):
        template = template_env.get_template('templates/index.html')
        context = {}
        self.response.write(template.render(context))


    def post(self):
        pass

class ContactHandler(webapp2.RequestHandler):
    def get(self):
        template = template_env.get_template('templates/contacts.html')
        context = {}
        self.response.write(template.render(context))

    def post(self):
        try:
            vstrNames = self.request.get('vstrNames')
            vstrEmail = self.request.get('vstrEmail')
            vstrCell = self.request.get('vstrCell')
            vstrSubject = self.request.get('vstrSubject')
            vstrMessage = self.request.get('vstrMessage')

            findRequest = Contact.query(Contact.strEmail == vstrEmail)
            thisContactList = findRequest.fetch()

            if len(thisContactList) > 0:
                thisContact = thisContactList[0]
            else:
                thisContact = Contact()

            thisContact.writeEmail(strinput=vstrEmail)
            thisContact.writeCell(strinput=vstrCell)
            thisContact.writeFullNames(strinput=vstrNames)
            thisContact.writeSubject(strinput=vstrSubject)
            thisContact.writeMessage(strinput=vstrMessage)
            thisContact.strMessageIndex = len(thisContactList)
            thisContact.put()
            self.response.write("Contact Message Submitted")
        except:
            self.response.write("Contact Message not Submitted")


class RegisterHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        template = template_env.get_template('templates/register.html')
        if Guser:
            findRequest = Profile.query(Profile.strReference == Guser.user_id())
            thisProfileList = findRequest.fetch()
            if len(thisProfileList) > 0:
                thisProfile = thisProfileList[0]
            else:
                thisProfile = Profile()

            if thisProfile.strProfileActivated:
                context = {'ProfileIsActive':"ProfileIsActive"}
            else:
                context = {}
            self.response.write(template.render(context))
        else:
            context = {}
            self.response.write(template.render(context))

class FAQHandler(webapp2.RequestHandler):
    def get(self):
        template = template_env.get_template('templates/faq.html')
        context = {}
        self.response.write(template.render(context))

class AboutHandler(webapp2.RequestHandler):
    def get(self):
        template = template_env.get_template("templates/about.html")
        context = {}
        self.response.write(template.render(context))

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        template = template_env.get_template('templates/login.html')
        context = {}
        self.response.write(template.render(context))

class TermsHandler(webapp2.RequestHandler):
    def get(self):
        template = template_env.get_template('templates/terms.html')
        context = {}
        self.response.write(template.render(context))
class PrivacyHandler(webapp2.RequestHandler):
    def get(self):
        template = template_env.get_template('templates/privacy.html')
        context = {}
        self.response.write(template.render(context))

class Error404Handler(webapp2.RequestHandler):
    def get(self):
        template = template_env.get_template('templates/404.html')
        context = {}
        self.response.write(template.render(context))

    def post(self):
        template = template_env.get_template('templates/404.html')
        context = {}
        self.response.write(template.render(context))


app = webapp2.WSGIApplication([

    ('/', MainHandler),
    ('/contact', ContactHandler),
    ('/register', RegisterHandler),
    ('/faq', FAQHandler),
    ('/login', LoginHandler),
    ('/about', AboutHandler),
    ('/terms', TermsHandler),
    ('/privacy', PrivacyHandler),
    ('/.*', Error404Handler)

], debug=True)
