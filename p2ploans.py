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

from profiles import Profile, Messages


class ActiveLoans(ndb.Expando):
    """
        Loans taken from my loan pocket
    """
    strReference = ndb.StringProperty()
    strTakenByReference = ndb.StringProperty()

    strLoanAmount = ndb.IntegerProperty()
    strDateTimeTaken = ndb.DateTimeProperty(auto_now_add=True)

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

    def writeTakenByReference(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strTakenByReference = strinput
                return True
            else:
                return False

        except:
            return False

    def writeLoanAmount(self,strinput):
        try:
            strinput = str(strinput)

            if strinput.isdigit():
                self.strLoanAmount = int(strinput)
                return True
            else:
                return False
        except:
            return False


class Myp2pPocket(ndb.Expando):
    """
        p2ploans here all available loans will be listed
    """
    strReference = ndb.StringProperty()
    strLoanPocket = ndb.IntegerProperty(default=0)

    strBalance = ndb.IntegerProperty(default=0)
    strLoanedOut = ndb.IntegerProperty(default=0)

    strInterest = ndb.IntegerProperty(default=15)
    strAutoLoan = ndb.BooleanProperty(default=True)

    strMyLoanLimit = ndb.IntegerProperty(default=0)
    strLimitAdjusted = ndb.BooleanProperty(default=False)



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
    def AddLoanPocket(self,strinput):
        try:
            strinput = str(strinput)

            if strinput.isdigit():
                self.strLoanPocket = self.strLoanPocket + int(strinput)
                return True
            else:
                return False
        except:
            return False
    def SubtractLoanPocket(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strLoanPocket = self.strLoanPocket - int(strinput)
                return True
            else:
                return False

        except:
            return False
    def writeInterest(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strInterest = int(strinput)
                return True
            else:
                return False
        except:
            return False
    def setAutoLoan(self):
        try:
            self.strAutoLoan = True
            return True
        except:
            return False
    def setManualLoan(self):
        try:
            self.strAutoLoan = False
            return True

        except:
            return False
    def AddBalance(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strBalance = self.strBalance + int(strinput)
                return True
            else:
                return False
        except:
            return False
    def SubtractBalance(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strBalance = self.strBalance - int(strinput)
                return True
            else:
                return False

        except:
            return False
    def AddLoanedOut(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strLoanedOut = self.strLoanedOut + int(strinput)
                return True
            else:
                return False

        except:
            return False
    def SubtractLoanedOut(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strLoanedOut = self.strLoanedOut - int(strinput)
                return True
            else:
                return False

        except:
            return False

class LoanRequests(ndb.Expando):
    strReference = ndb.StringProperty()
    strSendToReference = ndb.StringProperty()
    strRequestAmount = ndb.IntegerProperty(default=100)
    strDateTimeRequestSent = ndb.DateTimeProperty(auto_now_add=True)

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

    def writeSendToReference(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strSendToReference = strinput
                return True
            else:
                return False
        except:
            return False

    def writeRequestAmount(self,strinput):
        try:

            strinput = str(strinput)
            if strinput.isdigit():
                self.strRequestAmount = int(strinput)
                return True
            else:
                return False
        except:
            return False


class P2PLoansHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:

            findRequest = Myp2pPocket.query(Myp2pPocket.strReference == Guser.user_id())
            thisMyP2PPocketList = findRequest.fetch()

            if len(thisMyP2PPocketList) > 0:
                thisMyP2pPocket = thisMyP2PPocketList[0]
            else:
                thisMyP2pPocket = Myp2pPocket()
                thisMyP2pPocket.writeReference(strinput=Guser.user_id())
                thisMyP2pPocket.put()

            template = template_env.get_template('templates/admin/P2PLoans/p2ploans.html')
            context = {'thisMyP2pPocket':thisMyP2pPocket}
            self.response.write(template.render(context))

    def post(self):
        Guser = users.get_current_user()
        if Guser:
            vstrLoanPocket = self.request.get('vstrLoanPocket')
            vstrAllocate = self.request.get('vstrAllocate')

            findRequest = Myp2pPocket.query(Myp2pPocket.strReference == Guser.user_id())
            Myp2pPocketList = findRequest.fetch()

            if len(Myp2pPocketList) > 0:
                thisMyP2PPocket = Myp2pPocketList[0]
                if vstrAllocate == "YES":

                    findRequest = Profile.query(Profile.strReference == Guser.user_id())
                    thisProfileList = findRequest.fetch()

                    if len(thisProfileList) > 0:
                        thisProfile = thisProfileList[0]

                        if thisProfile.strWallet > int(vstrLoanPocket):
                            thisProfile.strWallet = thisProfile.strWallet - int(vstrLoanPocket)
                            thisProfile.put()


                            thisMyP2PPocket.writeReference(strinput=Guser.user_id())


                            thisMyP2PPocket.AddLoanPocket(strinput=vstrLoanPocket)
                            thisMyP2PPocket.put()
                            self.response.write("Loan Pocket Successfully Created")
                        else:
                            self.response.write("Insufficient Funds to Create a Loan Pocket")
                    else:
                        self.response.write("Create a Profile and fund it first before you can create a loan Pocket")
                else:

                    findRequest = Profile.query(Profile.strReference == Guser.user_id())
                    thisProfileList = findRequest.fetch()

                    if len(thisProfileList) > 0:
                        thisProfile = thisProfileList[0]
                    else:
                        thisProfile = Profile()
                        thisProfile.writeReference(strinput=Guser.user_id())
                        thisProfile.put()

                    findRequest = Myp2pPocket.query(Myp2pPocket.strReference == Guser.user_id())
                    thisMyP2PPocketList = findRequest.fetch()

                    if len(thisMyP2PPocketList) > 0:
                        thisMyP2PPocket = thisMyP2PPocketList[0]
                    else:
                        thisMyP2PPocket = Myp2pPocket()
                        thisMyP2PPocket.writeReference(strinput=Guser.user_id())
                        thisMyP2PPocket.put()

                    if thisMyP2PPocket.strBalance >= int(vstrLoanPocket):
                        try:
                            thisMyP2PPocket.strBalance = thisMyP2PPocket.strBalance - int(vstrLoanPocket)
                            thisMyP2PPocket.put()
                            thisProfile.strWallet = thisProfile.strWallet + int(vstrLoanPocket)
                            thisProfile.strTotalFundsReceived = thisProfile.strTotalFundsReceived + int(vstrLoanPocket)
                            thisProfile.put()
                            self.response.write("Succesfull Transferred Available funds into Wallet")
                        except:
                            self.response.write("Error transfering Available funds into Wallet")
                    else:
                        self.response.write("Insufficient funds to transfer into wallet")
            else:
                thisMyP2PPocket = Myp2pPocket()
                if vstrAllocate == "YES":

                    findRequest = Profile.query(Profile.strReference == Guser.user_id())
                    thisProfileList = findRequest.fetch()

                    if len(thisProfileList) > 0:
                        thisProfile = thisProfileList[0]

                        if thisProfile.strWallet > int(vstrLoanPocket):
                            thisProfile.strWallet = thisProfile.strWallet - int(vstrLoanPocket)
                            thisProfile.put()


                            thisMyP2PPocket.writeReference(strinput=Guser.user_id())


                            thisMyP2PPocket.writeLoanPocket(strinput=vstrLoanPocket)
                            thisMyP2PPocket.put()
                            self.response.write("Loan Pocket Successfully Created")
                        else:
                            self.response.write("Insufficient Funds to Create a Loan Pocket")
                    else:
                        self.response.write("Create a Profile and fund it first before you can create a loan Pocket")
                else:



                    thisMyP2PPocket.writeReference(strinput=Guser.user_id())

                    thisMyP2PPocket.writeLoanPocket(strinput=vstrLoanPocket)
                    thisMyP2PPocket.put()

class LoanRequestsHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:
            findRequests = LoanRequests.query(LoanRequests.strSendToReference == Guser.user_id())
            thisLoanRequestsList = findRequests.fetch()

            template = template_env.get_template('templates/admin/P2PLoans/LoanRequests.html')
            context = {'thisLoanRequestsList':thisLoanRequestsList}
            self.response.write(template.render(context))


class ActiveLoansHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:

            findRequest = ActiveLoans.query(ActiveLoans.strReference == Guser.user_id())
            thisActiveLoansList = findRequest.fetch()

            template = template_env.get_template('templates/admin/P2PLoans/ActiveLoans.html')
            context = {'thisActiveLoansList':thisActiveLoansList}
            self.response.write(template.render(context))

class AvailableLoansHandler(webapp2.RequestHandler):
    """
        Find a way to not retrieve own loans
    """
    def get(self):
        Guser = users.get_current_user()
        if Guser:

            findRequests = Myp2pPocket.query(Myp2pPocket.strLoanPocket >= 10)
            thisMyp2pPocketList = findRequests.fetch(limit=500)
            emptyList = []

            for thisMyp2pPocket in thisMyp2pPocketList:
                if thisMyp2pPocket.strReference <> Guser.user_id():
                    emptyList.append(thisMyp2pPocket)

            template = template_env.get_template('templates/admin/P2PLoans/AvailableLoans.html')
            context = {'thisMyp2pPocketList': emptyList}
            self.response.write(template.render(context))

class LoansTakenHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:
            findRequest = ActiveLoans.query(ActiveLoans.strReference == Guser.user_id())
            thisActiveLoansList = findRequest.fetch()

            template = template_env.get_template('templates/admin/P2PLoans/LoansTaken.html')
            context = {'thisActiveLoansList':thisActiveLoansList}
            self.response.write(template.render(context))

class ThisAvailableLoanHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:
            URL = self.request.url
            URLlist = URL.split("/")
            vstrReference = URLlist[len(URLlist) - 1]

            findRequests = Myp2pPocket.query(Myp2pPocket.strReference == vstrReference)
            thisMyp2pPocketList = findRequests.fetch()

            if len(thisMyp2pPocketList) > 0:
                thisMyp2pPocket = thisMyp2pPocketList[0]
            else:
                thisMyp2pPocket = Myp2pPocket()

            findRequests = Profile.query(Profile.strReference == vstrReference)
            thisLoanProfileList = findRequests.fetch()

            if len(thisLoanProfileList) > 0:
                thisLoanProfile = thisLoanProfileList[0]
            else:
                thisLoanProfile = Profile()

            findRequests = Myp2pPocket.query(Myp2pPocket.strReference == Guser.user_id())
            thisMyOwnp2pPocketList = findRequests.fetch()

            if len(thisMyOwnp2pPocketList) > 0:
                thisMyOwnp2pPocket = thisMyOwnp2pPocketList[0]
            else:
                thisMyOwnp2pPocket = Myp2pPocket()

            myTempCal = float(100)
            myTempCal = 1 + (myTempCal/thisMyOwnp2pPocket.strInterest)

            thisMyOwnp2pPocket.strMyLoanLimit = int(thisMyOwnp2pPocket.strLoanedOut * myTempCal)
            thisMyOwnp2pPocket.put()

            template = template_env.get_template('templates/admin/P2PLoans/thisAvailableLoan.html')
            context = {'thisMyp2pPocket':thisMyp2pPocket,'thisLoanProfile':thisLoanProfile,'thisMyOwnp2pPocket':thisMyOwnp2pPocket}
            self.response.write(template.render(context))


    def post(self):

        Guser = users.get_current_user()
        if Guser:

            URL = self.request.url
            URLlist = URL.split("/")
            vstrThisLoanReference = URLlist[len(URLlist) - 1]

            findRequests = Myp2pPocket.query(Myp2pPocket.strReference == vstrThisLoanReference)
            thisLoanPocketList = findRequests.fetch()

            if len(thisLoanPocketList) > 0:
                thisLoanPocket = thisLoanPocketList[0]
            else:
                thisLoanPocket = Myp2pPocket()

            findRequests = Profile.query(Profile.strReference == Guser.user_id())
            thisMyProfileList = findRequests.fetch()

            if len(thisMyProfileList) > 0:
                thisMyProfile = thisMyProfileList[0]
            else:
                thisMyProfile = Profile()


            findRequests = Myp2pPocket.query(Myp2pPocket.strReference == Guser.user_id())
            thisMyp2pPocketList = findRequests.fetch()

            if len(thisMyp2pPocketList) > 0:
                thisMyp2pPocket = thisMyp2pPocketList[0]
            else:
                thisMyp2pPocket = Myp2pPocket()

            if (thisMyp2pPocket.strMyLoanLimit > 0):

                if thisMyp2pPocket.strMyLoanLimit > thisLoanPocket.strLoanPocket:
                    thisLoanPocket.strLoanedOut = thisLoanPocket.strLoanedOut + thisLoanPocket.strLoanPocket
                    thisLoanPocket.strLoanPocket = 0
                    thisMyp2pPocket.strBalance = thisMyp2pPocket.strBalance + thisLoanPocket.strLoanPocket
                    thisMyp2pPocket.strMyLoanLimit = thisMyp2pPocket.strMyLoanLimit - thisLoanPocket.strLoanPocket
                    vstrLoanedAmount = thisLoanPocket.strLoanPocket
                else:
                    thisLoanPocket.strLoanedOut = thisLoanPocket.strLoanedOut + thisMyp2pPocket.strMyLoanLimit

                    thisLoanPocket.strLoanPocket = thisLoanPocket.strLoanPocket -  thisMyp2pPocket.strMyLoanLimit

                    thisMyp2pPocket.strBalance  = thisMyp2pPocket.strBalance + thisMyp2pPocket.strMyLoanLimit
                    thisMyp2pPocket.strMyLoanLimit = 0
                    vstrLoanedAmount = thisMyp2pPocket.strMyLoanLimit


                thisLoanPocket.put()
                thisMyProfile.put()
                thisMyp2pPocket.put()

                thisActiveLoan = ActiveLoans()
                thisActiveLoan.writeReference(strinput=thisLoanPocket.strReference)
                thisActiveLoan.writeTakenByReference(strinput=Guser.user_id())
                thisActiveLoan.writeLoanAmount(strinput=str(thisMyp2pPocket.strMyLoanLimit))
                thisActiveLoan.put()

                self.response.write("You where credit with a loan of : $ " + str(vstrLoanedAmount) + ".00")
            else:
                self.response.write("Your loan request was declined due to insufficient credit earn more credit by giving out loans")


class BestLoanFinanciersHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:

            findRequests = Myp2pPocket.query(Myp2pPocket.strReference <> Guser.user_id())
            thisMyp2pPocketList = findRequests.fetch(limit=500)


            template = template_env.get_template('templates/admin/P2PLoans/financiers.html')
            context = {'thisMyp2pPocketList':thisMyp2pPocketList}
            self.response.write(template.render(context))


class LoanLimitHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:

            findRequest = Profile.query(Profile.strReference == Guser.user_id())
            thisProfileLimit = findRequest.fetch()

            if len(thisProfileLimit) > 0:
                thisProfile = thisProfileLimit[0]
            else:
                thisProfile = Profile()

            if thisProfile.strWallet > 10:
                findRequest = Myp2pPocket.query(Myp2pPocket.strReference == Guser.user_id())
                thisMyp2pPocketList = findRequest.fetch()
                if len(thisMyp2pPocketList) > 0:
                    thisMyp2pPocket = thisMyp2pPocketList[0]
                else:
                    thisMyp2pPocket = Myp2pPocket()

                if not(thisMyp2pPocket.strLimitAdjusted):

                    thisMyp2pPocket.writeReference(strinput=Guser.user_id())
                    thisMyp2pPocket.strMyLoanLimit = 100
                    thisMyp2pPocket.strLimitAdjusted = True
                    thisMyp2pPocket.put()
                    self.response.write("P2P Loan Limit Succesfully Raised")
                else:
                    self.response.write("P2P Loan Limit cannot be granted as you where already granted a limit adjust")
            else:
                self.response.write("P2P Loan Limit cannot be raised please deposit at least $ 10.00 into your wallet")


class TransferAvailableToLoanPocketHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:
            vstrLoanPocket = self.request.get('vstrLoanPocket')
            findRequest = Myp2pPocket.query(Myp2pPocket.strReference == Guser.user_id())
            thisMyp2pPocketList = findRequest.fetch()

            if len(thisMyp2pPocketList) > 0:
                thisMyp2pPocket = thisMyp2pPocketList[0]
            else:
                thisMyp2pPocket = Myp2pPocket()
                thisMyp2pPocket.writeReference(strinput=Guser.user_id())
                thisMyp2pPocket.put()

            if thisMyp2pPocket.strBalance >= int(vstrLoanPocket):
                thisMyp2pPocket.strBalance = thisMyp2pPocket.strBalance - int(vstrLoanPocket)
                thisMyp2pPocket.strLoanPocket = thisMyp2pPocket.strLoanPocket + int(vstrLoanPocket)
                thisMyp2pPocket.put()
                self.response.write("Succesfully transferred all available funds into your Loan Pocket")
            else:
                self.response.write("Unable to transfer your available funds into your loan pocket")


class  FinancierMessagesHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:
            URL = self.request.uri
            URLlist = URL.split("/")
            vstrReference = URLlist[len(URLlist) - 1]
            logging.info(vstrReference)
            findRequest = Messages.query(Messages.strFromReference == Guser.user_id(), Messages.strToReference == vstrReference)
            thisMyMessagesList = findRequest.fetch()

            findRequest = Messages.query(Messages.strFromReference == vstrReference, Messages.strToReference == Guser.user_id())
            thisFinancierMessagesList = findRequest.fetch()

            vstrSelector = self.request.get('vstrSelector')
            if vstrSelector == "Message":

                template = template_env.get_template('templates/admin/profiles/messages/messages.html')

                context = {'thisMyMessagesList':thisMyMessagesList,'thisFinancierMessagesList':thisFinancierMessagesList,
                           'vstrReference':vstrReference}

                self.response.write(template.render(context))
            else:
                template = template_env.get_template('templates/admin/profiles/messages/LoanRequest.html')

                context = {'thisMyMessagesList':thisMyMessagesList,'thisFinancierMessagesList':thisFinancierMessagesList,
                           'vstrReference':vstrReference}

                self.response.write(template.render(context))

    def post(self):
        Guser = users.get_current_user()
        if Guser:
            vstrSubject = self.request.get('vstrSubject')
            vcomposetextarea = self.request.get('vcomposetextarea')
            vstrReference = self.request.get('vstrReference')

            thisMessage = Messages()
            thisMessage.writeFromReference(strinput=Guser.user_id())
            thisMessage.writeToReference(strinput=vstrReference)
            thisMessage.writeSubject(strinput=vstrSubject)
            thisMessage.writeMessage(strinput=vcomposetextarea)
            thisMessage.put()
            self.response.write("Message Successfully Sent")

class ListOfP2PLoansHandler(webapp2.RequestHandler):
    def get(self):

        findRequests = Myp2pPocket.query(Myp2pPocket.strLoanPocket >= 10)
        thisMyp2pPocketList = findRequests.fetch(limit=500)

        template = template_env.get_template('templates/admin/P2PLoans/public_p2ploans.html')
        context = {'thisMyp2pPocketList': thisMyp2pPocketList}
        self.response.write(template.render(context))

app = webapp2.WSGIApplication([
    ('/p2ploans', P2PLoansHandler),
    ('/p2ploans/loanrequests', LoanRequestsHandler),
    ('/p2ploans/activeloans', ActiveLoansHandler),
    ('/p2ploans/availableloans', AvailableLoansHandler),
    ('/p2ploans/availableloans/.*', ThisAvailableLoanHandler),
    ('/p2ploans/loanstaken', LoansTakenHandler),
    ('/p2ploans/financiers', BestLoanFinanciersHandler),
    ('/p2ploans/loanlimit', LoanLimitHandler),
    ('/p2ploans/transferavailloanpocket', TransferAvailableToLoanPocketHandler),
    ('/p2ploans/financiers/messages', FinancierMessagesHandler),
    ('/p2ploans/list', ListOfP2PLoansHandler)

], debug=True)

