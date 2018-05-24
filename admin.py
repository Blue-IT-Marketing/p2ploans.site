import os
import webapp2
import jinja2
from google.appengine.ext import ndb
from google.appengine.api import users
import datetime
from google.appengine.api import memcache
from google.appengine.api import mail
import logging
#Jinja Loader

template_env = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.getcwd()))

from profiles import Profile,Settings
from Wallet import TodaysPayments
from Contact import Contact

class ActivateHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:
            vstrFirstName = self.request.get('vstrFirstName')
            vstrSurname = self.request.get('vstrSurname')
            vstrCellNumber = self.request.get('vstrCellNumber')
            vstrEmail = self.request.get('vstrEmail')

            findRequest = Profile.query(Profile.strReference == Guser.user_id())
            thisProfileList = findRequest.fetch()

            if len(thisProfileList) > 0:
                thisProfile = thisProfileList[0]
            else:
                thisProfile = Profile()

            try:
                thisProfile.writeReference(strinput=Guser.user_id())
                thisProfile.writeFullNames(strinput=vstrFirstName)
                thisProfile.writeSurname(strinput=vstrSurname)
                thisProfile.writeCell(strinput=vstrCellNumber)
                thisProfile.writeEmail(strinput=vstrEmail)
                thisProfile.CreateConfirmCode()
                if thisProfile.sendActivationCode() == True:
                    thisProfile.put()
                    self.response.write("A Comfirmation Email has been sent please follow the instructions on the email to fully activate your account")
                else:
                    self.response.write("Send Mail Function causing a general Error please check your email address")
            except:
                self.response.write("There was an error sending a confirmation email please try again")


class ActivateCodeHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:
            template = template_env.get_template('templates/register.html')
            context = {'Activate': "Activate"}
            self.response.write(template.render(context))


    def post(self):
        Guser = users.get_current_user()
        if Guser:
            vstrActivationCode = self.request.get('vstrActivationCode')
            findRequest = Profile.query(Profile.strReference == Guser.user_id())
            thisProfileList = findRequest.fetch()
            if len(thisProfileList) > 0:
                thisProfile = thisProfileList[0]

                if thisProfile.strProfileActivated == False:
                    if thisProfile.ConfirmCode == vstrActivationCode:
                        thisProfile.strProfileActivated = True
                        thisProfile.put()
                        self.response.write("Your Profile was Successfully Activated thank you")
                    else:
                        self.response.write("Your Profile Activation Code do not match")
                else:
                    self.response.write("Your Profile is already Activated")
            else:
                self.response.write("You do not have a profile yet please send an activation request")

class AdminHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:
            template = template_env.get_template('templates/admin/admin/admin.html')
            context = {}
            self.response.write(template.render(context))

class AdminProfilesHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:
            findRequest = Profile.query()
            thisProfilesList = findRequest.fetch()

            template = template_env.get_template('templates/admin/admin/profiles.html')
            context = {'thisProfilesList':thisProfilesList}
            self.response.write(template.render(context))


class thisAdminProfilesHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:
            URL = self.request.uri
            URLlist = URL.split("/")
            vstrReference = URLlist[len(URLlist) - 1]

            findRequest = Profile.query(Profile.strReference == vstrReference)
            thisProfileList = findRequest.fetch()
            if len(thisProfileList) > 0:
                thisProfile = thisProfileList[0]


                findRequest = Settings.query(Settings.strReference == vstrReference)
                thisSettingsList = findRequest.fetch()
                if len(thisSettingsList) > 0:
                    thisSettings = thisSettingsList[0]
                else:
                    thisSettings = Settings()

                template = template_env.get_template('templates/admin/admin/thisProfile.html')
                context = {'thisProfile':thisProfile,'thisSettings':thisSettings}
                self.response.write(template.render(context))



class AdminWithDrawalsHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:

            findRequest = TodaysPayments.query()
            thisTodaysPaymentsList = findRequest.fetch()

            template = template_env.get_template('templates/admin/admin/thisWithDrawals.html')
            context = {'thisTodaysPaymentsList':thisTodaysPaymentsList}
            self.response.write(template.render(context))








class MessagingHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:

            findRequest = Contact.query(Contact.strResponded == False)
            thisContactList = findRequest.fetch()
            template = template_env.get_template('templates/admin/admin/contacts.html')
            context = {'thisContactList':thisContactList}
            self.response.write(template.render(context))

    def post(self):
        Guser = users.get_current_user()
        AppEmail = 'noreply@p2ptraders-app.appspotmail.com'
        if Guser:
            vstrToEmail = self.request.get('vstrToEmail')
            vstrSubject = self.request.get('vstrSubject')
            vstrcomposetextarea = self.request.get('vstrcomposetextarea')
            vstrMessageIndex = self.request.get('vstrMessageIndex')
            vstrMessageIndex = int(vstrMessageIndex)
            message = mail.EmailMessage()
            message.sender = AppEmail
            message.to = vstrToEmail
            message.subject = vstrSubject
            message.html = vstrcomposetextarea

            message.send()
            findRequest = Contact.query(Contact.strMessageIndex == vstrMessageIndex)
            thisContactList = findRequest.fetch()
            if len(thisContactList) > 0:
                thisContact = thisContactList[0]
                thisContact.strResponded = True
                thisContact.put()

                self.response.write("Response Successfully sent to recipient")

class AdminMessagingReadHandler(webapp2.RequestHandler):
    def get(self):
        URL = self.request.uri
        URLlist = URL.split("/")
        vstrMessageIndex = URLlist[len(URLlist) - 1]
        vstrMessageIndex = int(vstrMessageIndex)
        logging.info(vstrMessageIndex)

        findRequest = Contact.query(Contact.strMessageIndex == vstrMessageIndex)
        thisContactList = findRequest.fetch()
        if len(thisContactList) > 0:
            thisContact = thisContactList[0]
            template = template_env.get_template('templates/admin/admin/readMessage.html')
            context = {'thisContact':thisContact}
            self.response.write(template.render(context))
        else:
            thisContact = Contact()



app = webapp2.WSGIApplication([
    ('/activate', ActivateHandler),
    ('/activate/code', ActivateCodeHandler),
    ('/admin', AdminHandler),
    ('/admin/profiles', AdminProfilesHandler),
    ('/admin/profiles/.*', thisAdminProfilesHandler),
    ('/admin/withdrawals', AdminWithDrawalsHandler),
    ('/admin/messaging', MessagingHandler),
    ('/admin/messaging/read/.*', AdminMessagingReadHandler)
], debug=True)