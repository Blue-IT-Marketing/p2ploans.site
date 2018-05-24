import os
import webapp2
import jinja2
from google.appengine.ext import ndb
from google.appengine.api import users
from google.appengine.api import memcache
import datetime
import logging
#Jinja Loader
from profiles import Profile
from const import Constant
from profiles import MyLikesShares
template_env = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.getcwd()))



class Campaigns(ndb.Expando):

    strCampaignID = ndb.StringProperty()

    strCampaignName = ndb.StringProperty()
    strCampaignIntro = ndb.StringProperty()
    strCampaignBody = ndb.StringProperty()

    strCampaignURL = ndb.StringProperty()
    strInternalURL = ndb.StringProperty()

    strReference = ndb.StringProperty()

    strFundMe = ndb.IntegerProperty(default=50)
    strReceivedFunds = ndb.IntegerProperty(default=0)

    strIsBusiness = ndb.BooleanProperty()

    strStartDate = ndb.DateProperty()
    strEndDate = ndb.DateProperty()

    strActive = ndb.BooleanProperty(default=False)
    strBoost = ndb.IntegerProperty(default=0)  # Boost is from one to ten

    strPromoted = ndb.BooleanProperty(default=False)

    strLikes = ndb.IntegerProperty(default=0)
    strShares = ndb.IntegerProperty(default=0)


    def writeCampaignName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strCampaignName = strinput
                return True
            else:
                return False
        except:
            return False
    def writeCampaignIntro(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strCampaignIntro = strinput
                return True
            else:
                return False

        except:
            return False
    def writeCampaignBody(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strCampaignBody = strinput
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

    def writeCampaignURL(self,strinput):
        try:

            strinput = str(strinput)
            if strinput != None:
                self.strCampaignURL = strinput
                return True
            else:
                return False
        except:
            return False

    def writeInternalURL(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strInternalURL = strinput
                return True
            else:
                return False
        except:
            return False

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
    def writeFundMe(self, strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strFundMe = int(strinput)
                return True
            else:
                return False

        except:
            return False
    def setBusinessCampaign(self,strinput):
        try:
            if strinput == True:
                self.strIsBusiness = True
                return True
            else:
                self.strIsBusiness = False
                return True
        except:
            return False
    def setStartDate(self,strinput):
        try:

            if strinput != None:
                self.strStartDate = strinput
            return True
        except:
            return False
    def setEndDate(self,strinput):
        try:
            if strinput != None:
                self.strEndDate = strinput
                return True
            else:
                return False
        except:
            return False
    def setActive(self):
        try:
            self.strActive = True
            return True
        except:
            return False
    def setBoostLevel(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                if int(strinput) <= 10:
                    self.strBoost = self.strBoost + int(strinput)
                    if self.strBoost > 10:
                        self.strBoost = 10
                        return True
                    else:
                        return True
                else:
                    return False
            else:
                return False
        except:
            return False
    def AddToReceivedFunds(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strReceivedFunds = self.strReceivedFunds + int(strinput)
                return True
            else:
                return False
        except:
            return False




class LoadCampaignsHandler(webapp2.RequestHandler):
    """
            PromotedCampaignList
    """
    def get(self):

        findRequest = Campaigns.query(Campaigns.strCampaignName <> None)
        thisCampaignList = findRequest.fetch()


        findRequest = Campaigns.query(Campaigns.strPromoted == True,Campaigns.strActive == True)
        thisPromotedCampaignList = findRequest.fetch()

        findRequest = Campaigns.query(Campaigns.strActive == True).order(+Campaigns.strLikes).order(+Campaigns.strShares)
        thisTrendingCampaignsList = findRequest.fetch()

        template = template_env.get_template('templates/traders.html')
        context = {'thisCampaignList':thisCampaignList,'thisPromotedCampaignList':thisPromotedCampaignList,
                   'thisTrendingCampaignsList':thisTrendingCampaignsList}
        self.response.write(template.render(context))



class MyCampaignsHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:

            findRequest = Campaigns.query(Campaigns.strReference == Guser.user_id())
            thisCampaignsList = findRequest.fetch()

            template = template_env.get_template('templates/admin/campaigns/campaign.html')
            context = {'thisCampaignsList':thisCampaignsList}
            self.response.write(template.render(context))

class CreateCampaignsHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:
            vstrCampaignType = self.request.get('vstrCampaignType')
            vstrCampaignName = self.request.get('vstrCampaignName')
            vstrCampaignIntro = self.request.get('vstrCampaignIntro')
            vstrCampaignBody = self.request.get('vstrCampaignBody')
            vstrFundMe = self.request.get('vstrFundMe')


            findRequest = Constant.query(Constant.strReference == Guser.user_id())
            thisConstantList = findRequest.fetch()

            if len(thisConstantList) > 0:
                thisConstant = thisConstantList[0]
            else:
                thisConstant = Constant()


            findRequest = Campaigns.query(Campaigns.strReference == Guser.user_id())
            thisCampaignsList = findRequest.fetch()

            findRequest = Profile.query(Profile.strReference == Guser.user_id())
            thisProfileList = findRequest.fetch()

            if len(thisProfileList) > 0:
                thisProfile = thisProfileList[0]
            else:
                thisProfile = Profile()

            if (thisProfile.strWallet > thisConstant.strCampaignCost) or (len(thisCampaignsList) < thisConstant.strFreeCampaignAllowance):
                if len(thisCampaignsList) > thisConstant.strFreeCampaignAllowance:
                    thisProfile.strWallet = thisProfile.strWallet - thisConstant.strCampaignCost
                else:
                    pass
                try:
                    thisCampaign = Campaigns()
                    thisCampaign.writeReference(strinput=Guser.user_id())
                    thisCampaignID = str(Guser.user_id()) + str(len(thisCampaignsList))

                    thisCampaign.writeCampaignID(strinput=thisCampaignID)
                    thisPublicURL = "/campaigns/public/" + thisCampaignID
                    thisPublicURL =  thisConstant.strAppURL + thisPublicURL
                    thisCampaign.writeCampaignURL(strinput=thisPublicURL)
                    thisCampaign.writeCampaignName(strinput=vstrCampaignName)
                    if vstrCampaignType == "Personal":
                        thisCampaign.setBusinessCampaign(strinput=True)
                    else:
                        thisCampaign.setBusinessCampaign(strinput=False)

                    thisCampaign.writeCampaignIntro(strinput=vstrCampaignIntro)
                    thisCampaign.writeCampaignBody(strinput=vstrCampaignBody)
                    thisCampaign.writeFundMe(strinput=vstrFundMe)
                    thisCampaign.setActive()
                    StartDate = datetime.datetime.now()
                    StartDate = StartDate.date()
                    EndDate = datetime.date.today() + datetime.timedelta(+30)
                    thisCampaign.setStartDate(strinput=StartDate)
                    thisCampaign.setEndDate(strinput=EndDate)
                    thisInternalURL = "/campaigns/detail/" + thisCampaignID
                    thisCampaign.writeInternalURL(strinput=thisInternalURL)


                    thisCampaign.put()
                    self.response.write("Successfully created your Campaign")
                except:
                    self.response.write("Error Creating Campaign")
            else:
                self.response.write("Insufficient credit to create a new campaign")

    def post(self):
        Guser = users.get_current_user()
        if Guser:
            vstrCampaignType = self.request.get('vstrCampaignType')
            vstrCampaignName = self.request.get('vstrCampaignName')
            vstrCampaignIntro = self.request.get('vstrCampaignIntro')
            vstrCampaignBody = self.request.get('vstrCampaignBody')
            vstrFundMe = self.request.get('vstrFundMe')


            findRequest = Constant.query(Constant.strReference == Guser.user_id())
            thisConstantList = findRequest.fetch()

            if len(thisConstantList) > 0:
                thisConstant = thisConstantList[0]
            else:
                thisConstant = Constant()


            findRequest = Campaigns.query(Campaigns.strReference == Guser.user_id())
            thisCampaignsList = findRequest.fetch()

            findRequest = Profile.query(Profile.strReference == Guser.user_id())
            thisProfileList = findRequest.fetch()

            if len(thisProfileList) > 0:
                thisProfile = thisProfileList[0]
            else:
                thisProfile = Profile()

            if (thisProfile.strWallet > thisConstant.strCampaignCost) or (len(thisCampaignsList) < thisConstant.strFreeCampaignAllowance):
                if len(thisCampaignsList) > thisConstant.strFreeCampaignAllowance:
                    thisProfile.strWallet = thisProfile.strWallet - thisConstant.strCampaignCost
                else:
                    pass
                try:
                    thisCampaign = Campaigns()
                    thisCampaign.writeReference(strinput=Guser.user_id())
                    thisCampaignID = str(Guser.user_id()) + str(len(thisCampaignsList))

                    thisCampaign.writeCampaignID(strinput=thisCampaignID)
                    thisPublicURL = "/campaigns/public/" + thisCampaignID
                    thisPublicURL =  thisConstant.strAppURL + thisPublicURL
                    thisCampaign.writeCampaignURL(strinput=thisPublicURL)
                    thisCampaign.writeCampaignName(strinput=vstrCampaignName)
                    if vstrCampaignType == "Personal":
                        thisCampaign.setBusinessCampaign(strinput=True)
                    else:
                        thisCampaign.setBusinessCampaign(strinput=False)

                    thisCampaign.writeCampaignIntro(strinput=vstrCampaignIntro)
                    thisCampaign.writeCampaignBody(strinput=vstrCampaignBody)
                    thisCampaign.writeFundMe(strinput=vstrFundMe)
                    # thisCampaign.setActive() Cannot set the campaign to active since this is a draft
                    StartDate = datetime.datetime.now()
                    StartDate = StartDate.date()
                    EndDate = datetime.date.today() + datetime.timedelta(+30)
                    thisCampaign.setStartDate(strinput=StartDate)
                    thisCampaign.setEndDate(strinput=EndDate)
                    thisInternalURL = "/campaigns/detail/" + thisCampaignID
                    thisCampaign.writeInternalURL(strinput=thisInternalURL)


                    thisCampaign.put()
                    self.response.write("Successfully created your Campaign")
                except:
                    self.response.write("Error Creating Campaign")
            else:
                self.response.write("Insufficient credit to create a new campaign")

class DetailCampaignsHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:
            URL = self.request.uri
            URL = str(URL)
            URLlist = URL.split("/")
            vstrCampaignID = URLlist[len(URLlist) - 1]

            findRequest = Campaigns.query(Campaigns.strCampaignID == vstrCampaignID)
            thisCampaignList = findRequest.fetch()
            if len(thisCampaignList) > 0:
                thisCampaign = thisCampaignList[0]
            else:
                thisCampaign = Campaigns()

            template = template_env.get_template('templates/admin/campaigns/campaignDetail.html')
            context = {'thisCampaign':thisCampaign}
            self.response.write(template.render(context))


class ApplyBoostHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:
            vstrapply_boost = self.request.get('vstrapply_boost')
            vstrCampaignID = self.request.get('vstrCampaignID')

            findRequest = Campaigns.query(Campaigns.strCampaignID == vstrCampaignID)
            thisCampaignList = findRequest.fetch()

            if len(thisCampaignList) > 0:
                thisCampaign = thisCampaignList[0]
            else:
                thisCampaign = Campaigns()

            if (thisCampaign.strBoost + int(vstrapply_boost)) <= 10:

                findRequest = Profile.query(Profile.strReference == thisCampaign.strReference)
                thisProfileList = findRequest.fetch()
                if len(thisProfileList) > 0:
                    thisProfile = thisProfileList[0]
                else:
                    thisProfile = Profile()

                if thisProfile.strWallet > int(vstrapply_boost):
                    thisCampaign.setBoostLevel(strinput=vstrapply_boost)
                    thisProfile.strWallet = thisProfile.strWallet - int(vstrapply_boost)
                    thisProfile.put()
                    self.response.write("Boost Level Successfully Adjusted")
                else:
                    self.response.write("Boost Level not Adjusted insufficient funds")

            elif thisCampaign.strBoost < 10:
                vstrapply_boost = 10 - thisCampaign.strBoost
                findRequest = Profile.query(Profile.strReference == thisCampaign.strReference)
                thisProfileList = findRequest.fetch()
                if len(thisProfileList) > 0:
                    thisProfile = thisProfileList[0]
                else:
                    thisProfile = Profile()

                if thisProfile.strWallet > vstrapply_boost:
                    vstrapply_boost = str(vstrapply_boost)
                    thisCampaign.setBoostLevel(strinput=vstrapply_boost)
                    thisProfile.strWallet = thisProfile.strWallet - int(vstrapply_boost)
                    thisProfile.put()
                    self.response.write("Boost Level Successfully Adjusted")
                else:
                    self.response.write("Boost Level not Adjusted insufficient funds")

            else:
                self.response.write("Campaign fully boosted")

            thisCampaign.put()


    def post(self):
        Guser = users.get_current_user()
        if Guser:

            vstrCampaignID = self.request.get('vstrCampaignID')

            findRequest = Campaigns.query(Campaigns.strCampaignID == vstrCampaignID)
            thisCampaignList = findRequest.fetch()

            if len(thisCampaignList) > 0:
                thisCampaign = thisCampaignList[0]
            else:
                thisCampaign = Campaigns()

            if not(thisCampaign.strPromoted):
                findRequest = Constant.query(Constant.strReference == Guser.user_id())
                thisConstantList = findRequest.fetch()
                if len(thisConstantList) > 0:
                    thisConstant = thisConstantList[0]
                else:
                    thisConstant = Constant()

                thisConstant.writeReference(strinput=Guser.user_id())
                thisConstant.put()

                findRequest = Profile.query(Profile.strReference == Guser.user_id())
                thisProfileList = findRequest.fetch()
                if len(thisProfileList) > 0:
                    thisProfile = thisProfileList[0]
                else:
                    thisProfile = Profile()

                thisProfile.writeReference(strinput=Guser.user_id())

                if (thisProfile.strWallet > thisConstant.strPromotionCost):
                    thisProfile.strWallet = thisProfile.strWallet - thisConstant.strPromotionCost
                    thisCampaign.strPromoted = True
                    thisProfile.put()
                    thisCampaign.put()
                    self.response.write("Campaign Successfully Promoted")
                else:
                    self.response.write("Campaign cannot be promoted insufficient funds")
            else:
                self.response.write("Campaign Already Promoted")



class PublicCampaignHandler(webapp2.RequestHandler):
    def get(self):
        URL = self.request.url
        URL = str(URL)
        URLlist = URL.split("/")
        strCampaignID = URLlist[len(URLlist) - 1]
        findRequest = Campaigns.query(Campaigns.strCampaignID == strCampaignID)
        thisCampaignsList = findRequest.fetch()

        if len(thisCampaignsList) > 0:
            thisCampaign = thisCampaignsList[0]
        else:
            thisCampaign = Campaigns()


        template = template_env.get_template('templates/admin/campaigns/publicCampaignDetail.html')
        context = {'thisCampaign':thisCampaign}
        self.response.write(template.render(context))





class SendFundsCampaignHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:
            vstrSendFunding = self.request.get('vstrSendFunding')
            vstrCampaignID = self.request.get('vstrCampaignID')

            findRequest = Campaigns.query(Campaigns.strCampaignID == vstrCampaignID)
            thisCampaignList = findRequest.fetch()

            self.response.write("Send fund running...")

            if len(thisCampaignList) > 0:
                thisCampaign = thisCampaignList[0]
            else:
                thisCampaign = Campaigns()

            findRequest = Profile.query(Profile.strReference == Guser.user_id())
            thisProfileList = findRequest.fetch()

            if len(thisProfileList) > 0:
                thisProfile = thisProfileList[0]
            else:
                thisProfile = Profile()

            if thisProfile.strWallet > int(vstrSendFunding):
                thisProfile.strWallet = thisProfile.strWallet - int(vstrSendFunding)
                thisProfile.strTotalFundsSent = thisProfile.strTotalFundsSent + int(vstrSendFunding)
                thisProfile.put()
                thisCampaign.AddToReceivedFunds(strinput=vstrSendFunding)
                thisCampaign.put()

                try:
                    findRequest = Profile.query(Profile.strReference == thisCampaign.strReference)
                    thisReceiveProfileList = findRequest.fetch()

                    if len(thisReceiveProfileList) > 0:
                        thisReceiveProfile = thisReceiveProfileList[0]
                    else:
                        thisReceiveProfile = Profile()

                    thisReceiveProfile.strTotalFundsReceived = thisReceiveProfile.strTotalFundsReceived + int(vstrSendFunding)
                    thisReceiveProfile.put()

                    self.response.write("Succesfully Funded Campaign")
                except:
                    self.response.write("Error Funding Project")
            else:
                self.response.write("Error Funding Campaign Insufficient Funds")

class LikesCampaignsHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:
            vstrCampaignID = self.request.get('vstrCampaignID')
            vstrSelect = self.request.get('vstrSelect')

            findRequest = MyLikesShares.query(MyLikesShares.strReference == Guser.user_id(),MyLikesShares.strCampaignID == vstrCampaignID)
            thisLikesSharesList = findRequest.fetch()
            if len(thisLikesSharesList) > 0:
                thisLikesShares = thisLikesSharesList[0]
            else:
                thisLikesShares = MyLikesShares()

            thisLikesShares.writeReference(strinput=Guser.user_id())
            thisLikesShares.writeCampaignID(strinput=vstrCampaignID)

            findRequest = Campaigns.query(Campaigns.strCampaignID == vstrCampaignID)
            thisCampaignList = findRequest.fetch()

            if len(thisCampaignList) > 0:
                thisCampaign = thisCampaignList[0]
            else:
                thisCampaign = Campaigns()

            if vstrSelect == "Like":
                if not(thisLikesShares.strLiked):
                    thisLikesShares.strLiked = True
                    thisCampaign.strLikes = thisCampaign.strLikes + 1
                    self.response.write("Successfully Liked Campaign")
                else:
                    thisLikesShares.strLiked = False
                    thisCampaign.strLikes = thisCampaign.strLikes - 1
                    self.response.write("Successfully Un-Liked Campaign")

            else:
                thisLikesShares.strShared = True
                thisCampaign.strShares = thisCampaign.strShares + 1
                self.response.write("Campaign will be shared on your Wall")

            try:
                thisCampaign.put()
                thisLikesShares.put()
            except:
                pass






app = webapp2.WSGIApplication([
    ('/campaigns', LoadCampaignsHandler),
    ('/campaigns/mycampaigns', MyCampaignsHandler),
    ('/campaigns/create', CreateCampaignsHandler),
    ('/campaigns/detail/.*', DetailCampaignsHandler),
    ('/campaigns/applyboost', ApplyBoostHandler),
    ('/campaigns/public/.*', PublicCampaignHandler),
    ('/campaigns/sendfunds', SendFundsCampaignHandler),
    ('/campaigns/likes', LikesCampaignsHandler)
], debug=True)





