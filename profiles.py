import os
import webapp2
import jinja2
from google.appengine.ext import ndb
from google.appengine.api import users
from google.appengine.api import mail
import datetime,random,string


import logging
#Jinja Loader
template_env = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.getcwd()))


class MyLikesShares(ndb.Expando):
    strReference = ndb.StringProperty()
    strCampaignID = ndb.StringProperty()
    strLiked = ndb.BooleanProperty()
    strShared = ndb.BooleanProperty()

    def writeReference(self,strinput):
        try:
            strinput = str(strinput)

            if strinput != None:
                self.strReference = strinput
                return True
            else:
                return False

        except:
            return False


    def writeCampaignID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strCampaignID = strinput
                return True
            else:
                return False
        except:
            return False

class Settings(ndb.Expando):
    strReference = ndb.StringProperty()
    strAutoTrade = ndb.BooleanProperty(default=False)
    strAutoWithDraw = ndb.BooleanProperty(default=False)
    strBusinessProfile = ndb.BooleanProperty(default=False)
    strSendNotifications = ndb.BooleanProperty(default=False)
    strProfilePrivate = ndb.BooleanProperty(default=False)
    strAnonymous = ndb.BooleanProperty(default=False)


    def writeReference(self,strinput):
        try:
            strinput = str(strinput)

            if strinput != None:
                self.strReference = strinput
                return True
            else:
                return False

        except:
            return False

class Messages(ndb.Expando):

    strToReference = ndb.StringProperty()
    strFromReference = ndb.StringProperty()

    strMessageIndex = ndb.IntegerProperty()

    strMessageType = ndb.StringProperty(default="Message") # Note , Task
    strSubject = ndb.StringProperty()
    strMessage = ndb.StringProperty()
    strDateTimeSent = ndb.DateTimeProperty()
    strDateTimeRead = ndb.DateTimeProperty()


    def writeToReference(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strToReference = strinput
                return True
            else:
                return False
        except:
            return False
    def writeFromReference(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strFromReference = strinput
                return True
            else:
                return False

        except:
            return False
    def setNote(self):
        try:
            self.strMessageType = "Note"
            return True
        except:
            return False
    def SetMessage(self):
        try:
            self.strMessageType = "Message"
            return True
        except:
            return False
    def setTask(self):
        try:
            self.strMessageType = "Task"
            return True
        except:
            return False
    def writeSubject(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strSubject = strinput
                return True
            else:
                return False
        except:
            return False
    def writeMessage(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strMessage = strinput
                return True
            else:
                return False
        except:
            return False
    def setDateTimeSent(self):
        try:
            Today = datetime.datetime.now()
            self.strDateTimeSent = Today
            return True
        except:
            return False
    def setDateTimeRead(self):
        try:
            Today = datetime.datetime.now()
            self.strDateTimeRead = Today
            return True
        except:
            return False

class BankAccount(ndb.Expando):
    strReference = ndb.StringProperty()
    strAccountHolder = ndb.StringProperty()
    strBankName = ndb.StringProperty()
    strBranchCode = ndb.StringProperty()
    strAccountNumber = ndb.StringProperty()
    strAccountType = ndb.StringProperty()

    def writeReference(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strReference = strinput
                return True
            else:
                return False
        except:
            return False

    def writeAccountHolder(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAccountHolder = strinput
                return True
            else:
                return False
        except:
            return False

    def writeBankName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strBankName = strinput
                return True
            else:
                return False
        except:
            return False

    def writeBranchCode(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strBranchCode = strinput
                return True
            else:
                return False

        except:
            return False

    def writeAccountNumber(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAccountNumber = strinput
                return True
            else:
                return False

        except:
            return False

    def writeAccountType(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAccountType = strinput
                return True
            else:
                return False
        except:
            return False

class Profile(ndb.Expando):
    _maxConfirmCodeLen = 36
    _AppEmail = 'noreply@p2ptraders-app.appspotmail.com'
    ConfirmCode = ndb.StringProperty()
    strReference = ndb.StringProperty()
    strFullNames = ndb.StringProperty()
    strSurname = ndb.StringProperty()
    strNickname = ndb.StringProperty()

    strProfileName = ndb.StringProperty()
    strProfileIntro = ndb.StringProperty()
    strMyStory = ndb.StringProperty()

    strPayPalEmail = ndb.StringProperty()
    strEmail = ndb.StringProperty()
    strCell = ndb.StringProperty()

    strWebsite = ndb.StringProperty()

    strProfileActivated = ndb.BooleanProperty(default=False)


    strWallet = ndb.IntegerProperty(default=0)
    strWithdraw = ndb.IntegerProperty(default=0)
    strWithDrawMethod = ndb.StringProperty(default="PayPal") # Bank Account

    strTotalFundsSent = ndb.IntegerProperty(default=0)
    strTotalFundsReceived = ndb.IntegerProperty(default=0)

    strScheduleWithdrawal = ndb.DateProperty()

    strIDNumber = ndb.StringProperty()

    strTotalTrades = ndb.IntegerProperty(default=0)
    strTotalTradePartners = ndb.IntegerProperty(default=0)



    strTotalMessages = ndb.IntegerProperty(default=0)
    strTotalNotifications = ndb.IntegerProperty(default=0)
    strTotalTasks = ndb.IntegerProperty(default=0)

    strAvailableBoost = ndb.IntegerProperty(default=0)

    strLikes = ndb.IntegerProperty(default=0)

    def writeReference(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strReference = strinput
                return True
            else:
                return False

        except:
            return False
    def writeFullNames(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strFullNames = strinput
                return True
            else:
                return False
        except:
            return False

    def writeSurname(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strSurname = strinput
                return True
            else:
                return False

        except:
            return False
    def writeNickName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strNickname = strinput
                return True
            else:
                return False
        except:
            return False
    def writeProfileName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strProfileName = strinput
                return True
            else:
                return False
        except:
            return False
    def writePayPalEmail(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strPayPalEmail = strinput
                return True
            else:
                return False
        except:
            return False

    def writeEmail(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strEmail = strinput
                return True
            else:
                return False
        except:
            return False

    def writeCell(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strCell = strinput
                return True
            else:
                return False
        except:
            return False

    def writeWebsite(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strWebsite = strinput
                return True
            else:
                return False

        except:
            return False

    def writeIntroduction(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strProfileIntro = strinput
                return True
            else:
                return False
        except:
            return False
    def writeMyStory(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strMyStory = strinput
                return True
            else:
                return False

        except:
            return False
    def writeIDNumber(self,strinput):
        try:

            strinput = str(strinput)
            if strinput != None:
                self.strIDNumber = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTotalMessages(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strTotalMessages = int(strinput)
                return True
            else:
                return False

        except:
            return False
    def writeTotalNotifications(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strTotalNotifications = int(strinput)
                return True
            else:
                return False
        except:
            return False
    def writeTotalTasks(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strTotalTasks = int(strinput)
                return True
            else:
                return False

        except:
            return False

    def writeTotalTrades(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strTotalTrades = int(strinput)
                return True
            else:
                return False

        except:
            return False

    def writeTotalTradePartners(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strTotalTradePartners = int(strinput)
                return True
            else:
                return False
        except:
            return False

    def CreateConfirmCode(self):
        try:
            tkey = self.put()
            tkey = str(tkey)
            self.ConfirmCode = tkey[(len(tkey) - self._maxConfirmCodeLen): (len(tkey) - 1)]
            self.put()
            return self.ConfirmCode
        except:
            return self._generalError

    def getBody(self):
        try:

            BodyHTML = """
            <strong>In order for you to fully use the services of p2ptraders.com you have to activate your account</strong><br>
            <strong>You can activate your account by visiting the following link and then inputting the activation code below</strong><br>
            <strong>Activation Code : </strong>""" + self.ConfirmCode + """ <br>
            <br>
            <strong> Link : <a href="https://www.p2ptraders.com/activate/code">https://www.p2ptraders.com/activate/code</a> </strong><br>
            Thank you<br>
            https://p2ptraders.com

            """
            return BodyHTML
        except:
            return None

    def generate_activation_key(self,size=64, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))

    def generate_activation_url(self):
        return 'https://www.p2ptraders.com/profiles/activate/' + self.generate_activation_key()


    def sendActivationCode(self):
        try:
            message = mail.EmailMessage()
            message.sender = self._AppEmail
            message.to = self.strEmail
            message.subject = "p2ptraders.com activate your account"
            message.html = self.getBody()

            message.send()
            return True
        except:
            return None

class NewsLetter(ndb.Expando):
    strNewsLetterIndex = ndb.IntegerProperty(default=0)
    strSubject = ndb.StringProperty()
    strBody = ndb.StringProperty()

    def writeNewsLetterInder(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strNewsLetterIndex = int(strinput)
                return True
            else:
                return False
        except:
            return False


    def writeSubject(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strSubject = strinput
                return True
            else:
                return False
        except:
            return False

    def writeBody(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strBody = strinput
                return True
            else:
                return False
        except:
            return False



class EmailList(ndb.Expando):
    strListIndex = ndb.IntegerProperty(default=0)
    strReference = ndb.StringProperty()
    strEmail = ndb.StringProperty()
    strNames = ndb.StringProperty()
    strSurname = ndb.StringProperty()

    def writeListIndex(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strListIndex = int(strinput)
                return True
            else:
                return False
        except:
            return False
    def writeReference(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strReference = str(strinput)
                return True
            else:
                return False
        except:
            return False
    def writeEmail(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strEmail = str(strinput)
                return True
            else:
                return False
        except:
            return False
    def writeNames(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strNames = strinput
                return True
            else:
                return False
        except:
            return False
    def writeSurname(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strSurname = strinput
                return True
            else:
                return False
        except:
            return False


class LoadProfileHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:

            findRequest = Profile.query(Profile.strReference == Guser.user_id())
            thisProfileList = findRequest.fetch()
            if len(thisProfileList) > 0:
                thisProfile = thisProfileList[0]
            else:
                thisProfile = Profile()


            findRequest = Settings.query(Settings.strReference == Guser.user_id())
            thisSettingsList = findRequest.fetch()

            if len(thisSettingsList) > 0:
                thisSettings = thisSettingsList[0]
            else:
                thisSettings = Settings()

            template = template_env.get_template('templates/profiles.html')
            context = {'thisProfile':thisProfile,'thisSettings':thisSettings}
            self.response.write(template.render(context))

    def post(self):
        Guser = users.get_current_user()
        if Guser:

            findRequest = Profile.query().order(+Profile.strAvailableBoost)
            thisProfileList = findRequest.fetch(limit=1000)

            template = template_env.get_template('templates/admin/profiles/profile.html')
            context = {'thisProfileList': thisProfileList}
            self.response.write(template.render(context))


class BoostProfileHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:
            vstrBooster_1 = self.request.get('vstrBooster_1')

            findRequest = Profile.query(Profile.strReference == Guser.user_id())
            thisProfileList = findRequest.fetch()

            if len(thisProfileList) > 0:
                thisProfile = thisProfileList[0]
            else:
                thisProfile = Profile()

            thisProfile.writeReference(strinput=Guser.user_id())
            if thisProfile.strWallet > int(vstrBooster_1):
                thisProfile.strWallet = thisProfile.strWallet - int(vstrBooster_1)
                thisProfile.strAvailableBoost = thisProfile.strAvailableBoost + int(vstrBooster_1)
                thisProfile.put()
                self.response.write("Boost Succesfully bought : " + str(thisProfile.strAvailableBoost))
            else:
                self.response.write("Insufficient Credit to Purchase Boost")


class SaveProfileHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:
            vstrProfileName = self.request.get('vstrProfileName')
            vstrEmail = self.request.get('vstrEmail')
            vstrPayPalEmail = self.request.get('vstrPayPalEmail')
            vstrProfileIntroduction = self.request.get('vstrProfileIntroduction')

            findRequest = Profile.query(Profile.strReference == Guser.user_id())
            thisProfileList = findRequest.fetch()

            if len(thisProfileList) > 0:
                thisProfile = thisProfileList[0]
            else:
                thisProfile = Profile()

            try:

                thisProfile.writeReference(strinput=Guser.user_id())
                thisProfile.writeProfileName(strinput=vstrProfileName)
                thisProfile.writePayPalEmail(strinput=vstrPayPalEmail)
                thisProfile.writeEmail(strinput=vstrEmail)
                thisProfile.writeIntroduction(strinput=vstrProfileIntroduction)
                thisProfile.put()

                self.response.write("Profile Saved Succesfully")
            except:
                self.response.write("Error when Saving Profile")

class ProfileInboxHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:
            findRequest = Messages.query(Messages.strToReference == Guser.user_id())
            thisMessagesList = findRequest.fetch()
            TotalMessages = len(thisMessagesList)

            template = template_env.get_template('templates/admin/inbox/inbox.html')
            context = {'thisMessagesList':thisMessagesList,'TotalMessages':TotalMessages}
            self.response.write(template.render(context))

class ReadThisMessageHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:
            URL = str(self.request.uri)
            URLlist = URL.split("/")
            vstrMessageIndex = URLlist[len(URLlist) - 1]
            vstrMessageIndex = int(vstrMessageIndex)

            findRequest = Messages.query(Messages.strMessageIndex == vstrMessageIndex)
            thisMessagesList = findRequest.fetch()

            if len(thisMessagesList) > 0:
                thisMessage = thisMessagesList[0]
            else:
                thisMessage = Messages()

            template = template_env.get_template('templates/admin/inbox/thisMessage.html')
            context = {'thisMessage':thisMessage}
            self.response.write(template.render(context))




class ProfilesSettingsHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:
            vstrAutoTrade = self.request.get('vstrAutoTrade')
            vstrAutoWithDraw = self.request.get('vstrAutoWithDraw')
            vstrBussinessProfile = self.request.get('vstrBussinessProfile')
            vstrSendNotifications = self.request.get('vstrSendNotifications')
            vstrMakeProfilePrivate = self.request.get('vstrMakeProfilePrivate')
            vstrMakeChatPrivate = self.request.get('vstrMakeChatPrivate')


            findRequest = Settings.query(Settings.strReference == Guser.user_id())
            thisSettingsList = findRequest.fetch()

            if len(thisSettingsList) > 0:
                thisSettings = thisSettingsList[0]
            else:
                thisSettings = Settings()

            thisSettings.writeReference(strinput=Guser.user_id())
            if vstrAutoTrade == "YES":
                thisSettings.strAutoTrade = True

            if vstrAutoWithDraw == "YES":
                thisSettings.strAutoWithDraw = True

            if vstrBussinessProfile == "YES":
                thisSettings.strBusinessProfile = True

            if vstrSendNotifications == "YES":
                thisSettings.strSendNotifications = True

            if vstrMakeProfilePrivate == "YES":
                thisSettings.strProfilePrivate = True

            if vstrMakeChatPrivate == "YES":
                thisSettings.strAnonymous = True


            thisSettings.put()

            self.response.write("Settings Successfully Updated")




class ThisPublicProfileHandler(webapp2.RequestHandler):
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
            else:
                thisProfile = Profile()


            template = template_env.get_template('templates/admin/profiles/thisProfile.html')
            context = {'thisProfile':thisProfile}
            self.response.write(template.render(context))


class SendNewsLettersHandler(webapp2.RequestHandler):
    def get(self):
        pass

app = webapp2.WSGIApplication([
    ('/profiles', LoadProfileHandler),
    ('/profiles/boost', BoostProfileHandler),
    ('/profiles/save', SaveProfileHandler),
    ('/profiles/inbox', ProfileInboxHandler),
    ('/profiles/inbox/.*', ReadThisMessageHandler),
    ('/profiles/settings', ProfilesSettingsHandler),
    ('/profiles/public/.*', ThisPublicProfileHandler),
    ('/profiles/newsletters', SendNewsLettersHandler)

], debug=True)



