import os
import webapp2
import jinja2
from google.appengine.ext import ndb
from google.appengine.api import users
import datetime
from google.appengine.api import memcache

import logging
#Jinja Loader

template_env = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.getcwd()))

from profiles import Profile

class Affiliates(ndb.Expando):
    strReference = ndb.StringProperty()
    strAffiliateReference = ndb.StringProperty()
    strDateRegistered = ndb.DateTimeProperty(auto_now_add=True)
    strActivated = ndb.BooleanProperty(default=False)
    strSubscriptionAmount = ndb.IntegerProperty(default=20)

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
    def writeAffiliateReference(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAffiliateReference = strinput
                return True
            else:
                return False

        except:
            return False
    def setActivated(self):
        try:
            self.strActivated = True
            return True
        except:
            return False
    def setDeactivate(self):
        try:
            self.strActivated = False
            return True
        except:
            return False
    def writeSubscriptionAmount(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strSubscriptionAmount = int(strinput)
                return True
            else:
                return False

        except:
            return False

class MyStats(ndb.Expando):
    strReference = ndb.StringProperty()

    strStatsIndex = ndb.StringProperty()

    strThisDateTime = ndb.DateTimeProperty(auto_now_add=True)

    strTotalAffiliates = ndb.IntegerProperty(default=0)
    strSubscriptionIncome = ndb.IntegerProperty(default=0)
    strLoansIncome = ndb.IntegerProperty(default=0)
    strCrowdFundingIncome = ndb.IntegerProperty(default=0)
    strTotalIncome = ndb.IntegerProperty(default=0)


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

    def setStatsIndex(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strStatsIndex = strinput
                return True
            else:
                return False
        except:
            return False

    def setTotalAffiliates(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strTotalAffiliates = self.strTotalAffiliates + int(strinput)
                return True
            else:
                return False
        except:
            return False

    def setSubscriptionIncome(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strSubscriptionIncome = self.strSubscriptionIncome + int(strinput)
                return True
            else:
                return False
        except:
            return False

    def setLoansIncome(self,strinput):
        try:

            strinput = str(strinput)
            if strinput.isdigit():
                self.strLoansIncome = int(strinput)
                return True
            else:
                return False
        except:
            return False

    def setCrowdFundingIncome(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strCrowdFundingIncome = int(strinput)
                return True
            else:
                return False
        except:
            return False

    def setTotalIncome(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strTotalIncome = int(strinput)
                return True
            else:
                return False
        except:
            return False

class MyAffiliates(ndb.Expando):
    strReference = ndb.StringProperty()


    strTotalAffiliates = ndb.IntegerProperty(default=0)
    strSubscriptionIncome = ndb.IntegerProperty(default=0)
    strLoansIncome = ndb.IntegerProperty(default=0)
    strCrowdFundingIncome = ndb.IntegerProperty(default=0)
    strTotalIncome = ndb.IntegerProperty(default=0)
    strAvailable = ndb.IntegerProperty(default=0)

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
    def setTotalAffiliates(self, strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strTotalAffiliates = self.strTotalAffiliates + int(strinput)
                return True
            else:
                return False
        except:
            return False
    def setSubscriptionIncome(self, strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strSubscriptionIncome = self.strSubscriptionIncome + int(strinput)
                return True
            else:
                return False
        except:
            return False
    def setLoansIncome(self, strinput):
        try:

            strinput = str(strinput)
            if strinput.isdigit():
                self.strLoansIncome = int(strinput)
                return True
            else:
                return False
        except:
            return False
    def setCrowdFundingIncome(self, strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strCrowdFundingIncome = int(strinput)
                return True
            else:
                return False
        except:
            return False
    def setTotalIncome(self, strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strTotalIncome = int(strinput)
                return True
            else:
                return False
        except:
            return False
    def setAvailable(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strAvailable = self.strAvailable + int(strinput)
                return True
            else:
                return False
        except:
            return False

class LandingPage(ndb.Expando):
    strReference = ndb.StringProperty()
    strAffiliateLink = ndb.StringProperty(default="https://p2ptraders.com/affiliates/public/")

    strLPSEODescription = ndb.StringProperty(default="Edit your SEO Description in order to get a better listing on Google")
    strSEOTitle = ndb.StringProperty(default="Edit your SEO Title")

    strLPHeading = ndb.StringProperty(default="The Heading for your landing Page")
    strLPIntroduction = ndb.StringProperty(default="The introduction for your Landing Page")
    strLPBody = ndb.StringProperty(default="Body of your Landing Page")
    strLPFooter = ndb.StringProperty(default="Footer of your Landing Page")


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
    def writeAffiliateLink(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAffiliateLink = strinput
                return True
            else:
                return False
        except:
            return False
    def writeLPSEOTitle(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strSEOTitle = strinput
                return True
            else:
                return False
        except:
            return False
    def writeLPSEODescription(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strLPSEODescription = strinput
                return True
            else:
                return False
        except:
            return False
    def writeLPHeading(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strLPHeading = strinput
                return True
            else:
                return False
        except:
            return False
    def writeLPIntroduction(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strLPIntroduction = strinput
                return True
            else:
                return False
        except:
            return False
    def writeLPBody(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strLPBody = strinput
                return True
            else:
                return False
        except:
            return False
    def writeLPFooter(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strLPFooter = strinput
                return True
            else:
                return False
        except:
            return False





class Promotions(ndb.Expando):
    strReference = ndb.StringProperty()
    strPriorityListing = ndb.IntegerProperty(default=3)
    strEnablePriorityListing = ndb.BooleanProperty(default=False)
    strAutoDownLine = ndb.IntegerProperty(default=3)
    strEnableAutoDownLine = ndb.BooleanProperty(default=False)
    strSocialMediaPromo = ndb.IntegerProperty(default=3)
    strEnableSocialMediaPromo = ndb.BooleanProperty(default=False)

    strTotalPromos = ndb.IntegerProperty(default=0)

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
    def setPriorityListingValue(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strPriorityListing = int(strinput)
                return True
            else:
                return False
        except:
            return False
    def enablePriorityListing(self):
        try:
            self.strEnablePriorityListing = True
            return True
        except:
            return False
    def setAutoDownLineValue(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strAutoDownLine = int(strinput)
                return True
            else:
                return False
        except:
            return False
    def enableAutoDownLine(self):
        try:
            self.strEnableAutoDownLine = True
            return True
        except:
            return False
    def setSocialMediaPromoValue(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strSocialMediaPromo = int(strinput)
                return True
            else:
                return False
        except:
            return False
    def enableSocialMediaPromo(self):
        try:
            self.strEnableSocialMediaPromo = True
            return True
        except:
            return False

class Subscriptions(ndb.Expando):
    strReference = ndb.StringProperty()
    strAutoRenewAffiliate = ndb.BooleanProperty(default=False)
    strAutoRenewPromos = ndb.BooleanProperty(default=False)
    strAutoRenewDate = ndb.IntegerProperty(default=30)

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
    def setAutoRenewAffiliate(self):
        try:
            self.strAutoRenewAffiliate = True
            return True
        except:
            return False
    def setAutoRenewPromos(self):
        try:
            self.strAutoRenewPromos = True
            return True
        except:
            return False
    def setAutoRenewDate(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strAutoRenewDate = int(strinput)
                return True
            else:
                return False
        except:
            return False


class AffiliatesHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:

            findRequests = Affiliates.query(Affiliates.strReference == Guser.user_id())
            thisAffiliatesList = findRequests.fetch()

            findRequests = MyStats.query(MyStats.strReference == Guser.user_id())
            thisMyStatsList = findRequests.fetch()

            findRequests = MyAffiliates.query(MyAffiliates.strReference == Guser.user_id())
            thisMyAffiliatesList = findRequests.fetch()

            if len(thisMyAffiliatesList) > 0:
                thisMyAffiliates = thisMyAffiliatesList[0]
            else:
                thisMyAffiliates = MyAffiliates()
                thisMyAffiliates.writeReference(strinput=Guser.user_id())
                thisMyAffiliates.put()






            template = template_env.get_template('templates/admin/Affiliate/affiliate.html')
            context = {'thisAffiliatesList':thisAffiliatesList,'thisMyStatsList':thisMyStatsList,'thisMyAffiliates':thisMyAffiliates}
            self.response.write(template.render(context))
class FullstatsHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:

            findRequests = MyStats.query(MyStats.strReference == Guser.user_id())
            thisMyStatsList = findRequests.fetch()


            template = template_env.get_template('templates/admin/Affiliate/fullstats.html')
            context = {'thisMyStatsList':thisMyStatsList}
            self.response.write(template.render(context))
class MyAffiliatesHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:
            findRequests = Affiliates.query(Affiliates.strReference == Guser.user_id())
            thisAffiliatesList = findRequests.fetch()


            template = template_env.get_template('templates/admin/Affiliate/myaffiliates.html')
            context = {'thisAffiliatesList':thisAffiliatesList}
            self.response.write(template.render(context))
class PromosHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:

            findRequest = Promotions.query(Promotions.strReference == Guser.user_id())
            thisPromotionsList = findRequest.fetch()

            if len(thisPromotionsList) > 0:
                thisPromotions = thisPromotionsList[0]
            else:
                thisPromotions = Promotions()
                thisPromotions.writeReference(strinput=Guser.user_id())
                thisPromotions.put()


            template = template_env.get_template('templates/admin/Affiliate/promos.html')
            context = {'thisPromotions':thisPromotions}
            self.response.write(template.render(context))
class SubscriptionsHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:
            findRequest = Subscriptions.query(Subscriptions.strReference == Guser.user_id())
            thisSubscriptionsList = findRequest.fetch()

            if len(thisSubscriptionsList) > 0:
                thisSubscriptions = thisSubscriptionsList[0]
            else:
                thisSubscriptions = Subscriptions()
                thisSubscriptions.writeReference(strinput=Guser.user_id())
                thisSubscriptions.put()

            template = template_env.get_template('templates/admin/Affiliate/subscriptions.html')
            context = {'thisSubscriptions':thisSubscriptions}
            self.response.write(template.render(context))

    def post(self):
        Guser = users.get_current_user()
        if Guser:
            findRequest = Subscriptions.query(Subscriptions.strReference == Guser.user_id())
            thisSubscriptionsList = findRequest.fetch()

            if len(thisSubscriptionsList) > 0:
                thisSubscriptions = thisSubscriptionsList[0]
            else:
                thisSubscriptions = Subscriptions()
                thisSubscriptions.writeReference(strinput=Guser.user_id())
                thisSubscriptions.put()

            vstrChoice = self.request.get('vstrChoice')
            vstrAutoRenewDate = self.request.get('vstrAutoRenewDate')


            if vstrChoice == "Affiliate":
                thisSubscriptions.strAutoRenewAffiliate = not(thisSubscriptions.strAutoRenewAffiliate)
                thisSubscriptions.setAutoRenewDate(strinput=vstrAutoRenewDate)
                thisSubscriptions.put()
                self.response.write("Successfully set affiliate subscriptions on Auto Renew")
            else:
                thisSubscriptions.strAutoRenewPromos = not(thisSubscriptions.strAutoRenewPromos)
                thisSubscriptions.setAutoRenewDate(strinput=vstrAutoRenewDate)
                thisSubscriptions.put()
                self.response.write("Successfully set Promotions subscriptions on Auto Renew")




class SettingsHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:
            findRequest = LandingPage.query(LandingPage.strReference == Guser.user_id())
            thisLandingPageList = findRequest.fetch()
            if len(thisLandingPageList) > 0:
                thisLandingPage = thisLandingPageList[0]
            else:
                thisLandingPage = LandingPage()
                thisLandingPage.writeReference(strinput=Guser.user_id())
                thisLandingPage.put()

            template = template_env.get_template('templates/admin/Affiliate/LandingPage.html')
            context = {'thisLandingPage':thisLandingPage}
            self.response.write(template.render(context))

    def post(self):
        Guser = users.get_current_user()
        if Guser:
            vstrSelector = self.request.get('vstrSelector')
            findRequest = LandingPage.query(LandingPage.strReference == Guser.user_id())
            thisLandingPageList = findRequest.fetch()

            if len(thisLandingPageList) > 0:
                thisLandingPage = thisLandingPageList[0]
            else:
                thisLandingPage = LandingPage()
                thisLandingPage.writeReference(strinput=Guser.user_id())
                thisLandingPage.put()



            if vstrSelector == "Link":
                thisLink = "https://p2ptraders.com/affiliates/public/" + Guser.user_id()
                thisLandingPage.writeAffiliateLink(strinput=thisLink)
                thisLandingPage.put()
                template = template_env.get_template("templates/admin/Affiliate/settingsAFLink.html")
                context = {'thisLandingPage':thisLandingPage}
                self.response.write(template.render(context))
            elif vstrSelector == "SEOTitle":
                template = template_env.get_template("templates/admin/Affiliate/settingsSEOTitle.html")
                context = {'thisLandingPage':thisLandingPage}
                self.response.write(template.render(context))
            elif vstrSelector == "SEODescription":
                template = template_env.get_template("templates/admin/Affiliate/settingsSEODescription.html")
                context = {'thisLandingPage':thisLandingPage}
                self.response.write(template.render(context))
            elif vstrSelector == "LPHeading":
                template = template_env.get_template("templates/admin/Affiliate/LPHeading.html")
                context = {'thisLandingPage':thisLandingPage}
                self.response.write(template.render(context))
            elif vstrSelector == "LPIntro":
                template = template_env.get_template("templates/admin/Affiliate/LPIntro.html")
                context = {'thisLandingPage':thisLandingPage}
                self.response.write(template.render(context))
            elif vstrSelector == "LPBody":
                template = template_env.get_template("templates/admin/Affiliate/LPBody.html")
                context = {'thisLandingPage':thisLandingPage}
                self.response.write(template.render(context))
            elif vstrSelector == "LPFooter":
                template = template_env.get_template("templates/admin/Affiliate/LPFooter.html")
                context = {'thisLandingPage':thisLandingPage}
                self.response.write(template.render(context))










class EnablePriorityHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:
            findRequests = Promotions.query(Promotions.strReference == Guser.user_id())
            thisPromotionsList = findRequests.fetch()

            if len(thisPromotionsList) > 0:
                thisPromotions = thisPromotionsList[0]
            else:
                thisPromotions = Promotions()
                thisPromotions.writeReference(strinput=Guser.user_id())
                thisPromotions.put()

            findRequests = Profile.query(Profile.strReference == Guser.user_id())
            thisProfileList = findRequests.fetch()

            if len(thisProfileList) > 0:
                thisProfile = thisProfileList[0]
            else:
                thisProfile = Profile()
                thisProfile.writeReference(strinput=Guser.user_id())
                thisProfile.put()


            if thisProfile.strWallet > thisPromotions.strPriorityListing:
                thisProfile.strWallet = thisProfile.strWallet - thisPromotions.strPriorityListing
                thisProfile.put()
                thisPromotions.strEnablePriorityListing = True
                thisPromotions.strTotalPromos = thisPromotions.strTotalPromos +  thisPromotions.strPriorityListing
                thisPromotions.put()
                self.response.write("Priority Listing Enabled")
            else:
                self.response.write("Failed to enable Priority Listing- Insufficient funds")

    def post(self):
        Guser = users.get_current_user()
        if Guser:

            findRequests = Promotions.query(Promotions.strReference == Guser.user_id())
            thisPromotionsList = findRequests.fetch()

            if len(thisPromotionsList) > 0:
                thisPromotions = thisPromotionsList[0]
            else:
                thisPromotions = Promotions()
                thisPromotions.writeReference(strinput=Guser.user_id())
                thisPromotions.put()

            if thisPromotions.strEnablePriorityListing == True:
                thisPromotions.strEnablePriorityListing = False
                thisPromotions.strTotalPromos = thisPromotions.strTotalPromos - thisPromotions.strPriorityListing
                thisPromotions.put()
                self.response.write("Priority Listing Disabled")
            else:
                self.response.write("Priority Listing Already Disabled")
class EnableAutoDownLineHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:

            findRequest = Promotions.query(Promotions.strReference == Guser.user_id())
            thisPromotionsList = findRequest.fetch()

            if len(thisPromotionsList) > 0:
                thisPromotions = thisPromotionsList[0]
            else:
                thisPromotions = Promotions()
                thisPromotions.writeReference(strinput=Guser.user_id())
                thisPromotions.put()

            findRequest = Profile.query(Profile.strReference == Guser.user_id())
            thisProfileList = findRequest.fetch()

            if len(thisProfileList) > 0:
                thisProfile = thisProfileList[0]
            else:
                thisProfile = Profile()
                thisProfile.writeReference(strinput=Guser.user_id())
                thisProfile.put()

            if thisProfile.strWallet > thisPromotions.strAutoDownLine:
                thisProfile.strWallet = thisProfile.strWallet - thisPromotions.strAutoDownLine
                thisProfile.put()
                thisPromotions.strEnableAutoDownLine = True
                thisPromotions.strTotalPromos = thisPromotions.strTotalPromos +  thisPromotions.strAutoDownLine
                thisPromotions.put()
                self.response.write("Auto Down-Line Enabled")
            else:
                self.response.write("Failed to enable Auto Down-Line - Insufficient Funds")

    def post(self):
        Guser = users.get_current_user()
        if Guser:

            findRequest = Promotions.query(Promotions.strReference == Guser.user_id())
            thisPromotionsList = findRequest.fetch()

            if len(thisPromotionsList) > 0:
                thisPromotions = thisPromotionsList[0]
            else:
                thisPromotions = Promotions()
                thisPromotions.writeReference(strinput=Guser.user_id())
                thisPromotions.put()


            if thisPromotions.strEnableAutoDownLine:
                thisPromotions.strEnableAutoDownLine =False
                thisPromotions.strTotalPromos = thisPromotions.strTotalPromos - thisPromotions.strAutoDownLine
                thisPromotions.put()
                self.response.write("Auto Down-Line Disabled Succesfully")
            else:
                self.response.write("Auto Down-Line Already Disabled")
class EnableSocialMediaPromosHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:


            findRequest = Promotions.query(Promotions.strReference == Guser.user_id())
            thisPromotionsList = findRequest.fetch()

            if len(thisPromotionsList) > 0:
                thisPromotions = thisPromotionsList[0]
            else:
                thisPromotions = Promotions()
                thisPromotions.writeReference(strinput=Guser.user_id())
                thisPromotions.put()

            findRequest = Profile.query(Profile.strReference == Guser.user_id())
            thisProfileList = findRequest.fetch()

            if len(thisProfileList) > 0:
                thisProfile = thisProfileList[0]
            else:
                thisProfile = Profile()
                thisProfile.writeReference(strinput=Guser.user_id())
                thisProfile.put()

            if thisProfile.strWallet > thisPromotions.strSocialMediaPromo:
                thisProfile.strWallet = thisProfile.strWallet - thisPromotions.strSocialMediaPromo
                thisProfile.put()
                thisPromotions.strEnableSocialMediaPromo = True
                thisPromotions.strTotalPromos = thisPromotions.strTotalPromos + thisPromotions.strSocialMediaPromo
                thisPromotions.put()
                self.response.write("Social Media Promos Enabled")
            else:
                self.response.write("Failure enabling Social Media Promos - Insufficient Funds")

    def post(self):
        Guser = users.get_current_user()
        if Guser:


            findRequest = Promotions.query(Promotions.strReference == Guser.user_id())
            thisPromotionsList = findRequest.fetch()

            if len(thisPromotionsList) > 0:
                thisPromotions = thisPromotionsList[0]
            else:
                thisPromotions = Promotions()
                thisPromotions.writeReference(strinput=Guser.user_id())
                thisPromotions.put()

            if thisPromotions.strEnableSocialMediaPromo:
                thisPromotions.strEnableSocialMediaPromo = False
                thisPromotions.strTotalPromos = thisPromotions.strTotalPromos - thisPromotions.strSocialMediaPromo
                thisPromotions.put()
                self.response.write("Social Media Promotions Enabled")
            else:
                self.response.write("Social Media Promotions Already Disabled")

class TransferFundsToWalletHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:
            findRequest = MyAffiliates.query(MyAffiliates.strReference == Guser.user_id())
            thisMyAffiliatesList = findRequest.fetch()

            if len(thisMyAffiliatesList) > 0:
                thisMyAffiliates = thisMyAffiliatesList[0]
            else:
                thisMyAffiliates = MyAffiliates()
                thisMyAffiliates.writeReference(strinput=Guser.user_id())
                thisMyAffiliates.put()

            if thisMyAffiliates.strAvailable >= 50:
                findRequest = Profile.query(Profile.strReference == Guser.user_id())
                thisProfileList = findRequest.fetch()
                if len(thisProfileList) > 0:
                    thisProfile = thisProfileList[0]
                else:
                    thisProfile = Profile()
                    thisProfile.writeReference(strinput=Guser.user_id())
                    thisProfile.put()
                try:
                    thisProfile.strWallet = thisProfile.strWallet + thisMyAffiliates.strAvailable
                    thisMyAffiliates.strAvailable = 0
                    thisProfile.strTotalFundsReceived = thisProfile.strTotalFundsReceived + thisMyAffiliates.strAvailable
                    thisMyAffiliates.put()
                    thisProfile.put()
                    self.response.write("Succesfully Transferred all Affiliate Income into your Wallet")
                except:
                    self.response.write("Error Transferring your Affiliate funds into your Wallet")
            else:
                self.response.write("Error Transferring your Affiliate funds into your Wallet insufficient credit")


class PublicAffiliateHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:

            URL = str(self.request.uri)
            URList = URL.split("/")
            vstrReference = URList[len(URList) - 1]

            findRequest = LandingPage.query(LandingPage.strReference == vstrReference)
            thisSettingsList = findRequest.fetch()

            if len(thisSettingsList) > 0:
                thisSettings = thisSettingsList[0]
            else:
                thisSettings = LandingPage()

            template = template_env.get_template('templates/admin/Affiliate/public/thisAffiliate.html')
            context = {'thisSettings':thisSettings}
            self.response.write(template.render(context))





class LandingPageDesignHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:
            vstrSelector = self.request.get('vstrSelector')

            findRequest = LandingPage.query(LandingPage.strReference == Guser.user_id())
            thisSettingsList = findRequest.fetch()

            if len(thisSettingsList) > 0:
                thisSettings = thisSettingsList[0]
            else:
                thisSettings = LandingPage()
                thisSettings.writeReference(strinput=Guser.user_id())

            if vstrSelector =="SEOTitle":
                vstrSEOTitle = self.request.get('vstrSEOTitle')
                thisSettings.writeLPSEOTitle(strinput=vstrSEOTitle)
                thisSettings.put()
                self.response.write("SEO Title Updated")
            elif vstrSelector == "SEODescription":
                vstrSEODescription = self.request.get('vstrSEODescription')
                thisSettings.writeLPSEODescription(strinput=vstrSEODescription)
                thisSettings.put()
                self.response.write("SEO Description Updated Successfully")
            elif vstrSelector == "LPBody":
                vstrLPBody = self.request.get('vstrLPBody')
                thisSettings.writeLPBody(strinput=vstrLPBody)
                thisSettings.put()
                self.response.write("Landing Page Body Updated Successfully")
            elif vstrSelector == "LPHeading":
                vstrLPHeading = self.request.get('vstrLPHeading')
                thisSettings.writeLPHeading(strinput=vstrLPHeading)
                thisSettings.put()
                self.response.write("Landing Page Heading Updated Successfully")
            elif vstrSelector == "LPIntro":
                vstrLPIntro = self.request.get('vstrLPIntro')
                thisSettings.writeLPIntroduction(strinput=vstrLPIntro)
                thisSettings.put()
                self.response.write("Landing Page Introduction Updated Successfully")
            elif vstrSelector =="LPFooter":
                vstrLPFooter = self.request.get('vstrLPFooter')
                thisSettings.writeLPFooter(strinput=vstrLPFooter)
                thisSettings.put()
                self.response.write("Landing Page Footer Updated Successfully")

    def post(self):
        Guser = users.get_current_user()
        if Guser:
            findRequest = LandingPage.query(LandingPage.strReference == Guser.user_id())
            thisLandingPageList = findRequest.fetch()
            if len(thisLandingPageList) > 0:
                thisLandingPage = thisLandingPageList[0]
            else:
                thisLandingPage = LandingPage()






app = webapp2.WSGIApplication([
    ('/affiliates', AffiliatesHandler),
    ('/affiliates/fullstats', FullstatsHandler),
    ('/affiliates/myaffiliates', MyAffiliatesHandler),
    ('/affiliates/promos', PromosHandler),
    ('/affiliates/settings', SettingsHandler),
    ('/affiliates/subscriptions', SubscriptionsHandler),
    ('/affiliates/enablepriority', EnablePriorityHandler),
    ('/affiliates/enableautodownline', EnableAutoDownLineHandler),
    ('/affiliates/enablesocialmedia', EnableSocialMediaPromosHandler),
    ('/affiliates/transfertowallet', TransferFundsToWalletHandler),
    ('/affiliates/public/.*', PublicAffiliateHandler),
    ('/affiliates/landingpage', LandingPageDesignHandler),




], debug=True)