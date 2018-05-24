import os
import webapp2
import jinja2
from google.appengine.ext import ndb
from google.appengine.api import users
import datetime
from google.appengine.api import memcache
import urllib, urllib2,httplib
from google.appengine.api import urlfetch
import logging
#Jinja Loader

template_env = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.getcwd()))

sandBoxMode = True
if sandBoxMode:
    PP_URL = "https://www.sandbox.paypal.com/cgi-bin/webscr"
    ACCOUNT_EMAIL= "mobiusndou@gmail.com"
else:
    PP_URL = "https://www.paypal.com/cgi-bin/webscr"
    ACCOUNT_EMAIL = "mobiusndou@gmail.com"

class PayPalPayments(ndb.Expando):
    strReference = ndb.StringProperty()
    strPayPalTransactionID = ndb.StringProperty()
    strPayMentEmail = ndb.StringProperty()
    strTransactionStatus = ndb.StringProperty()
    strInvoiceID = ndb.StringProperty()
    strCurrency = ndb.StringProperty()
    strAmount = ndb.StringProperty()
    strFee = ndb.StringProperty()
    strPayerID = ndb.StringProperty()
    strPayerEmail = ndb.StringProperty()
    strDateTimeOFTransaction = ndb.DateTimeProperty(auto_now_add=True)


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


    def writeTransactionID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strPayPalTransactionID = strinput
                return True
            else:
                return False
        except:
            return False

    def writePaymentEmail(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strPayMentEmail = strinput
                return True
            else:
                return False
        except:
            return False

    def writeTransactionStatus(self,strinput):
        try:
            strinput = str(strinput)

            if (strinput.lower() == "completed") or (strinput.lower() == "pending") or (strinput.lower() == "failed"):
                self.strTransactionStatus = strinput.lower()
                return True
            else:
                return False
        except:
            return False


    def writeInvoiceID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput == None:
                self.strInvoiceID = strinput
                return True
            else:
                return False
        except:
            return False




    def writeCurrency(self,strinput):
        try:
             strinput = str(strinput)
             #TODO-Consider testing for actual currency strings
             if strinput != None:
                 self.strCurrency = strinput
                 return True
             else:
                 return False
        except:
            return False



    def writeAmount(self,strinput):
        try:
            strinput = str(strinput)
            #TODO-Consider testing for actual values
            if (strinput == None):
                self.strAmount = strinput
                return True
            else:
                return False
        except:
            return False



    def writeFee(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strFee = strinput
                return True
            else:
                return False
        except:
            return False



    def writePayerID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strPayerID = strinput
                return True
            else:
                return False
        except:
            return False



    def writePayerEmail(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strPayerEmail = strinput
                return True
            else:
                return False
        except:
            return False

    def retrieveTransactionsByReference(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                findQuery = PayPalPayments.query(PayPalPayments.strReference == strinput)
                results = findQuery.fetch()
                if len(results) > 0:
                    return results
                else:
                    return None
            else:
                return None
        except:
            return None

    def retrieveTransactionsByTransactionID(self,strinput):
        try:
            strinput = str(strinput)

            if strinput != None:
                findQuery = PayPalPayments.query(PayPalPayments.strPayPalTransactionID == strinput)
                results = findQuery.fetch()
                if len(results) > 0:
                    return results
                else:
                    return None
            else:
                return  None
        except:
            return None

    def retrieveTransactionsByPaymentEmail(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                findQuery = PayPalPayments.query(PayPalPayments.strPayMentEmail == strinput)
                results = findQuery.fetch()
                if len(results) > 0:
                    return results
                else:
                    return None
            else:
                return None
        except:
            return None

    def retrieveTransactionsByTransactionStatus(self,strinput):
        try:
            strinput = str(strinput)

            if (strinput == "completed") or (strinput == "pending") or (strinput == "failed"):
                findQuery = PayPalPayments.query(PayPalPayments.strTransactionStatus == strinput)
                results = findQuery.fetch()
                if len(results) > 0:
                    return results
                else:
                    return None
            else:
                return None
        except:
            return None

    def storePayPalPayments(self):
        try:

            self.put()
            return True
        except:
            return False




class PayPalIPNHandler(webapp2.RequestHandler):
    def post(self):
        try:
            Guser = users.get_current_user()
            if Guser:
                parameters = None
                PayPalPay = PayPalPayments()
                # Check payment is completed, not Pending or Failed.
                PayPalPay.writeReference(strinput=Guser.user_id())
                if self.request.get('payment_status') == 'Completed':
                    if self.request.POST:
                        parameters = self.request.POST.copy()
                        PayPalPay.writeTransactionStatus(strinput="completed")
                    if self.request.GET:
                        parameters = self.request.GET.copy()
                        logging.debug("IPN verification Executing")
                        PayPalPay.writeTransactionStatus(strinput="pending")
                    else:
                        self.response.out.write("Error Sorry the Parameter was not complited")
                        PayPalPay.writeTransactionStatus(strinput="failed")

                    #TODO- Check the IPN POST request came from real PayPal,
                    #TODO- Not from a Fraudster.

                    if parameters:
                        parameters['cmd'] = '_notify-validate'

                    params = urllib.urlencode(parameters)

                    status = urlfetch.fetch(
                        url=PP_URL,
                        method=urlfetch.POST,
                        payload=params,
                    ).content

                    if not(status == "VERIFIED"):
                        template = template_env.get_template('templates/deposit.html')
                        context = {'Message': "Error IPN not Verified"}
                        self.response.write(template.render(context))
                    else:
                        parameters['homemadeParameterValidity']=False

                        # parameters = None
                        # You may log this data in your database,
                        # for later investigation.
                        # Check the money is really to go to your account,
                        # not to a fraudster's account.

                        if parameters['receiver_email'] == ACCOUNT_EMAIL:
                            transaction_id = parameters['txn_id']
                            PayPalPay.writePaymentEmail(strinput=ACCOUNT_EMAIL)
                            PayPalPay.writeTransactionID(strinput=transaction_id)

                            # Check if this is a new, unique txn,
                            # not a fraudster re-using an old, verified txn.

                            invoice_id = parameters['invoice']
                            PayPalPay.writeInvoiceID(strinput=invoice_id)
                            currency = parameters['mc_currency']
                            PayPalPay.writeCurrency(strinput=currency)
                            amount = parameters['mc_gross']
                            PayPalPay.writeAmount(strinput=amount)
                            fee = parameters['mc_fee']
                            PayPalPay.writeFee(strinput=fee)


                            # Check if they are the right product/item, right price,
                            # right currency, right amount, etc.

                            email = parameters['payer_email']
                            PayPalPay.writePayerEmail(strinput=email)
                            identifier = parameters['payer_id']
                            PayPalPay.writePayerID(strinput=identifier)

                            if PayPalPay.storePayPalPayments():


                                template = template_env.get_template('templates/deposit.html')
                                context = {'strTransactionStatus': "OK a Record of this Transaction has also been sent to your email",
                                           'strTransactionID': transaction_id,
                                           'strInvoiceID': invoice_id,
                                           'strPayerEmail': email}
                                self.response.write(template.render(context))

                                # Email/notify/inform the user for whatever reason.
                                parameters['your_parm'] = "It is ok on 19 September, 2010."
                                logging.debug('IPN 100. All OK.')
                                logging.debug(parameters['txn_id'])
                                logging.debug(parameters['invoice'])
                                logging.debug(parameters['payer_email'])
                                # With this IPN testing, you can't see results on the browser.
                                # See results on the log file maintained by Google AppEngine.

                        else:
                            template = template_env.get_template('templates/deposit.html')
                            context = {'strTransactionStatus': "Transaction unsuccesfull"}
                            self.response.write(template.render(context))


                else: # Payment Status is not Complete
                    template = template_env.get_template('templates/deposit.html')
                    context = {'strTransactionStatus': "Transaction unsuccesfull"}
                    self.response.write(template.render(context))
            else:
                template = template_env.get_template('templates/deposit.html')
                context = {'strTransactionStatus': "Transaction unsuccesfull"}
                self.response.write(template.render(context))
        except:
            template = template_env.get_template('templates/deposit.html')
            context = {'strTransactionStatus': "Transaction unsuccesfull"}
            self.response.write(template.render(context))


class DepositSuccesfulHandler(webapp2.RequestHandler):
    """
        if the user gets redirected here the deposit was succesful
        <form method=post action="https://www.paypal.com/cgi-bin/webscr">
            <input type="hidden" name="cmd" value="_notify-synch">
            <input type="hidden" name="tx" value="TransactionID">
            <input type="hidden" name="at" value="QieZsRoNf8Fmt3XVZx6AMKKuQs5SC2NIpmfNFrCM7Aiw5RHbk20ye7C0kiS">
            <input type="submit" value="PDT">
        </form>
    """
    def get(self):
        try:

            thisTX = self.request.get('tx')

            params = urllib.urlencode({'cmd': "_notify-synch", 'tx': thisTX, 'at': "QieZsRoNf8Fmt3XVZx6AMKKuQs5SC2NIpmfNFrCM7Aiw5RHbk20ye7C0kiS"})
            headers = {"Content-type": "application/x-www-form-urlencoded",
                       "Accept": "text/plain"}
            conn = httplib.HTTPConnection("https://www.paypal.com/cgi-bin/webscr")
            conn.request("POST", "", params, headers)
            response = conn.getresponse()
            thisContent = response.read()
            self.response.write(thisContent)
        except:
            self.response.write("Error")


    def post(self):
        self.response.write("Transaction worked")

class DepositCancelledHandler(webapp2.RequestHandler):
    def get(self):

        template = template_env.get_template('templates/admin/paypal/paymentcancelled.html')
        context = {}
        self.response.write(template.render(context))
    def post(self):
        self.response.write("Deposit was cancelled")

app = webapp2.WSGIApplication([
    ('/depositsuccesful', DepositSuccesfulHandler),
    ('/depositcancelled', DepositCancelledHandler),
    ('/paypalIPN0485234hhisidf683475bknbjsdf9843', PayPalIPNHandler)
], debug=True)
