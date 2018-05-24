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

from profiles import Profile, BankAccount

class TodaysPayments(ndb.Expando):

    strReference = ndb.StringProperty()
    strAmountToPay = ndb.IntegerProperty(default=0)
    strPaidAmount = ndb.IntegerProperty(default=0)
    strFullyPaid = ndb.StringProperty(default=False)
    strPayMethod = ndb.StringProperty(default="PayPal") # Bank

    strPayPalEmail = ndb.StringProperty()

    strAccountHolder = ndb.StringProperty()
    strBankName = ndb.StringProperty()
    strAccountNumber = ndb.StringProperty()
    strBranchCode = ndb.StringProperty()
    strAccountType = ndb.StringProperty(default="Savings")

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
    def writeAmountToPay(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strAmountToPay = int(strinput)
                return True
            else:
                return False
        except:
            return False
    def writePaidAmount(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strPaidAmount = int(strinput)
                return True
            else:
                return False
        except:
            return False
    def setFullyPaid(self):
        try:
            self.strFullyPaid = True
            return True
        except:
            return False
    def writePayMethod(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strPayMethod = strinput
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





class WalletHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:
            findRequest = Profile.query(Profile.strReference == Guser.user_id())
            thisProfileList = findRequest.fetch()

            if len(thisProfileList) > 0:
                thisProfile = thisProfileList[0]
            else:
                thisProfile = Profile()

            findRequest = BankAccount.query(BankAccount.strReference == Guser.user_id())
            thisBankAccountList = findRequest.fetch()
            if len(thisBankAccountList) > 0:
                thisBankAccount = thisBankAccountList[0]
            else:
                thisBankAccount = BankAccount()

                thisBankAccount.writeReference(strinput=Guser.user_id())
                thisBankAccount.put()

            template = template_env.get_template("templates/admin/wallet/wallet.html")
            context = {'thisProfile':thisProfile,'thisBankAccount':thisBankAccount}
            self.response.write(template.render(context))

    def post(self):
        Guser = users.get_current_user()
        if Guser:
            findRequest = Profile.query(Profile.strReference == Guser.user_id())
            thisProfileList = findRequest.fetch()

            if len(thisProfileList) > 0:
                thisProfile = thisProfileList[0]
            else:
                thisProfile = Profile()
                thisProfile.writeReference(strinput=Guser.user_id())

            vstrPayPalEmail = self.request.get('vstrPayPalEmail')

            infoUpdated = False

            if not(vstrPayPalEmail == None):
                thisProfile.writePayPalEmail(strinput=vstrPayPalEmail)
                thisProfile.put()
                infoUpdated = True

            vstrAccountHolder = self.request.get('vstrAccountHolder')
            vstrBankName = self.request.get('vstrBankName')
            vstrBranchCode = self.request.get('vstrBranchCode')
            vstrAccountNumber = self.request.get('vstrAccountNumber')
            vstrAccountType = self.request.get('vstrAccountType')

            if ((not(vstrAccountHolder == None)) and (not(vstrAccountNumber == None))):
                findRequest = BankAccount.query(BankAccount.strReference == Guser.user_id())
                thisBankAccountList = findRequest.fetch()
                if len(thisBankAccountList) > 0:
                    thisBankAccount = thisBankAccountList[0]
                else:
                    thisBankAccount = BankAccount()
                    thisBankAccount.writeReference(strinput=Guser.user_id())

                thisBankAccount.writeAccountHolder(strinput=vstrAccountHolder)
                thisBankAccount.writeBankName(strinput=vstrBankName)
                thisBankAccount.writeBranchCode(strinput=vstrBranchCode)
                thisBankAccount.writeAccountType(strinput=vstrAccountType)

                thisBankAccount.put()
                infoUpdated = True



            if infoUpdated:
                self.response.write("Account Linking Information is successfully updated")
            else:
                self.response.write("Account Linking Information not updated we will not be able to process your withdrawals successfully")







class WalletWithdrawHandler(webapp2.RequestHandler):

    def get(self):
        Guser = users.get_current_user()
        if Guser:
            vstrWithDrawalAmount = self.request.get('vstrWithDrawalAmount')
            vstrWithdrawalMethod = self.request.get('vstrWithdrawalMethod')
            vstrWithDrawalAmount = int(vstrWithDrawalAmount)

            findRequest = Profile.query(Profile.strReference == Guser.user_id())
            thisProfileList = findRequest.fetch()

            if len(thisProfileList) > 0:
                thisProfile = thisProfileList[0]
            else:
                thisProfile = Profile()

            thisProfile.writeReference(strinput=Guser.user_id())

            if (thisProfile.strWallet > vstrWithDrawalAmount) and (vstrWithDrawalAmount > 100):
                thisProfile.strWallet = thisProfile.strWallet - vstrWithDrawalAmount
                thisProfile.strWithdraw = thisProfile.strWithdraw + vstrWithDrawalAmount
                Today = datetime.datetime.now()
                Today = Today.date()

                thisMonth = Today.month
                thisYear = Today.year

                if thisMonth < 12:
                    thisMonth = thisMonth + 1
                else:
                    thisMonth = 1
                    thisYear = thisYear + 1

                thisDay = Today.day

                Today = datetime.date(year=thisYear,month=thisMonth,day=thisDay)

                thisProfile.strScheduleWithdrawal = Today
                thisProfile.strWithDrawMethod = vstrWithdrawalMethod
                thisProfile.put()

                self.response.write("Withdrawal Successfully scheduled")
            else:
                self.response.write("Cannot Schedule a withdrawal either because your withdrawal is less than $ 100.00 or your Balance is less than $ 100.00")
class CancelWithdrawalHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:

            findRequest = Profile.query(Profile.strReference == Guser.user_id())
            thisProfileList = findRequest.fetch()

            if len(thisProfileList) > 0:
                thisProfile = thisProfileList[0]

                if thisProfile.strWithdraw > 0:
                    thisProfile.strWallet = thisProfile.strWallet + thisProfile.strWithdraw
                    thisProfile.strWithdraw = 0
                    thisProfile.strScheduleWithdrawal = None
                    thisProfile.put()
                    self.response.write("Withdrawal Succesfully Cancelled")
                else:
                    self.response.write("Theres no Scheduled withdrawals to Cancell")
            else:

                self.response.write("Theres no Scheduled withdrawals to Cancell")


class PayTodayCronJobHandler(webapp2.RequestHandler):
    """
        Goes through all the Wallets and take off the amounts that are suppose to be paid that day
        store them on the list of pending payments to be accessed by Admins

        ....
        The Scheduled Payments will be taken off the Wallet


        strScheduleWithdrawal

    """
    def get(self):

        thisDay = datetime.datetime.today()
        thisDay = thisDay.date()
        findRequest = Profile.query(Profile.strScheduleWithdrawal == thisDay)
        thisProfileList = findRequest.fetch()

        for thisProfile in thisProfileList:

            if thisProfile.strWithdraw >= 100:
                thisPayments = TodaysPayments()
                thisPayments.writeAmountToPay(strinput=str(thisProfile.strWithdraw))
                thisPayments.writeReference(strinput=thisProfile.strReference)
                if thisProfile.strWithDrawMethod == "PayPal":
                    thisPayments.writePayMethod(strinput=thisProfile.strWithDrawMethod)
                    thisPayments.writePayPalEmail(strinput=thisProfile.strPayPalEmail)

                    try:
                        thisPayments.put()
                    except:
                        pass
                    thisProfile.strWithdraw = 0

                    thisProfile.put()



                else:
                    findRequest = BankAccount.query(BankAccount.strReference == thisProfile.strReference)
                    thisBankAccountList = findRequest.fetch()
                    if len(thisBankAccountList) > 0:
                        thisBankAccount = thisBankAccountList[0]
                    else:
                        thisBankAccount = BankAccount()
                        thisBankAccount.writeReference(strinput=thisProfile.strReference)
                        thisBankAccount.put()
                    try:
                        thisPayments.writeBankName(strinput=thisBankAccount.strBankName)
                        thisPayments.writeAccountHolder(strinput=thisBankAccount.strAccountHolder)
                        thisPayments.writeAccountNumber(strinput=thisBankAccount.strAccountNumber)
                        thisPayments.writeAccountType(strinput=thisBankAccount.strAccountType)
                        thisPayments.writeBranchCode(strinput=thisBankAccount.strBranchCode)
                        thisPayments.put()

                    except:
                        pass

                    thisProfile.strWithdraw = 0
                    thisProfile.strScheduleWithdrawal = None
                    thisProfile.put()




app = webapp2.WSGIApplication([
    ('/wallet', WalletHandler),
    ('/wallet/withdraw', WalletWithdrawHandler),
    ('/wallet/cancelwithdrawal', CancelWithdrawalHandler),
    ('/wallet/cron/paytoday',PayTodayCronJobHandler )

], debug=True)

