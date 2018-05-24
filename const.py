import os
import webapp2
import jinja2
from google.appengine.ext import ndb
from google.appengine.api import users
import logging
tEnviron = os.environ.copy()
if tEnviron['SERVER_SOFTWARE'] == 'Development/2.0':
    isGoogleServer = False
    logging.info('THIS IS A DEVELOPMENT SERVER')
else:
    logging.info('THIS IS A GOOGLE SERVER')
    isGoogleServer = True

class Constant(ndb.Expando):
    strReference = ndb.StringProperty()
    strCampaignCost = ndb.IntegerProperty(default=5)
    strFreeCampaignAllowance = ndb.IntegerProperty(default=2)
    strTotalActiveCampaigns = ndb.IntegerProperty(default=0)
    strAppURL = ndb.StringProperty(default="https://www.p2ploans.site")
    strPromotionCost = ndb.IntegerProperty(default=5)

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