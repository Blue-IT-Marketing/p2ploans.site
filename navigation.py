import os
import webapp2
import jinja2
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.api import memcache

import logging
#Jinja Loader
from profiles import Profile
template_env = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.getcwd()))


class HeaderHandler(webapp2.RequestHandler):
    """
        The header handler must

            Load Messages ,
            Notifications,
            Tasks,

        and also the Login/Logout options
    """

    def get(self):
        Guser = users.get_current_user()
        if Guser:
            vstrUsername = Guser.nickname()
            vstrLogoutURL = users.create_logout_url(dest_url="/")
            findRequest = Profile.query(Profile.strReference == Guser.user_id())
            thisProfileList = findRequest.fetch()


            if len(thisProfileList) > 0:
                thisProfile = thisProfileList[0]
                template = template_env.get_template('templates/dynamic/navigation/header.html')
                context = {'vstrUsername': thisProfile.strProfileName, 'vstrLogoutURL': vstrLogoutURL}
                self.response.write(template.render(context))

            else:
                template = template_env.get_template('templates/dynamic/navigation/header.html')
                context = {'vstrUsername': vstrUsername, 'vstrLogoutURL': vstrLogoutURL}
                self.response.write(template.render(context))
        else:
            vstrLoginURL = users.create_login_url(dest_url="/")

            template = template_env.get_template('templates/dynamic/navigation/header.html')
            context = {'vstrLoginURL': vstrLoginURL}
            self.response.write(template.render(context))

class SideBarHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        vstrLogoutURL = users.create_logout_url(dest_url="/")
        vstrLoginURL = users.create_login_url(dest_url="/")

        if Guser:
            vstrUsername = Guser.nickname()
            findRequest = Profile.query(Profile.strReference == Guser.user_id())
            thisProfileList = findRequest.fetch()

            if len(thisProfileList) > 0:
                thisProfile = thisProfileList[0]
                template = template_env.get_template('templates/dynamic/navigation/sidebar.html')
                context = {'vstrUsername': thisProfile.strProfileName,
                           'vstrLogoutURL': vstrLogoutURL,'strActivated': thisProfile.strProfileActivated}
                self.response.write(template.render(context))

            else:
                template = template_env.get_template('templates/dynamic/navigation/sidebar.html')
                context = {'vstrUsername': vstrUsername,
                           'vstrLogoutURL': vstrLogoutURL}
                self.response.write(template.render(context))
        else:
            template = template_env.get_template('templates/dynamic/navigation/sidebar.html')
            context = {'vstrLoginURL': vstrLoginURL}
            self.response.write(template.render(context))

class FooterHandler(webapp2.RequestHandler):
    def get(self):
        template = template_env.get_template('templates/dynamic/navigation/footer.html')
        context = {}
        self.response.write(template.render(context))


class StepHeaderHandler(webapp2.RequestHandler):

    def get(self):
        Guser = users.get_current_user()
        if Guser:
            vstrUsername = Guser.nickname()
            vstrLogoutURL = users.create_logout_url(dest_url="/")

            template = template_env.get_template('templates/dynamic/navigation/stepheader.html')
            context = {'vstrUsername': vstrUsername, 'vstrLogoutURL': vstrLogoutURL}
            self.response.write(template.render(context))
        else:
            vstrLoginURL = users.create_login_url(dest_url="/")

            template = template_env.get_template('templates/dynamic/navigation/header.html')
            context = {'vstrLoginURL': vstrLoginURL}
            self.response.write(template.render(context))


class NavAffHeaderHandler(webapp2.RequestHandler):
    def get(self):
        template = template_env.get_template('templates/admin/public/nav/header.html')
        context = {}
        self.response.write(template.render(context))


class NavAffSidebarHandler(webapp2.RequestHandler):
    def get(self):
        template = template_env.get_template('templates/admin/public/nav/sidebar.html')
        context = {}
        self.response.write(template.render(context))




app = webapp2.WSGIApplication([
    ('/navigation/header', HeaderHandler),
    ('/navigation/step/header', StepHeaderHandler),
    ('/navigation/sidebar', SideBarHandler),
    ('/navigation/footer', FooterHandler),
    ('/navigation/affiliate/header', NavAffHeaderHandler),
    ('/navigation/affiliate/sidebar', NavAffSidebarHandler)
], debug=True)
