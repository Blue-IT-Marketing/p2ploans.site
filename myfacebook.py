#-*- coding: utf-8 -*-
import time
from facepy import GraphAPI
import os
import webapp2
import jinja2
from google.appengine.ext import ndb
from google.appengine.api import users
template_env = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.getcwd()))


class MyGroupIDS(ndb.Expando):
    strReference = ndb.StringProperty()
    strGroupID = ndb.StringProperty()
    isWorking = ndb.BooleanProperty(default=False)

    def writeReference(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strReference = strinput
                return True
            else:
                return False
        except:
            return False

    def writeGroupID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strGroupID = strinput
                return True
            else:
                return False
        except:
            return False

    def setWorked(self):
        try:
            self.isWorking = True
            return True
        except:
            return False


class GroupPosts(ndb.Expando):
    strReference = ndb.StringProperty()
    strApiKey = ndb.StringProperty()
    strMyPost = ndb.StringProperty()

    def writeReference(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strReference = strinput
                return True
            else:
                return False
        except:
            return False

    def writeApiKey(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strApiKey = strinput
                return True
            else:
                return False
        except:
            return False

    def writeMyPost(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strMyPost = strinput
                return True
            else:
                return False
        except:
            return False


class FacebookGroupHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:
            vstrGraphApiKey = self.request.get('vstrGraphApiKey')
            vstrFacebookPost = self.request.get('vstrFacebookPost')
            vstrGroupIDs = self.request.get('vstrGroupIDs')

            GroupIDList = vstrGroupIDs.split(" ")

            findRequest = MyGroupIDS.query(MyGroupIDS.strReference == Guser.user_id())
            thisGroupIDList = findRequest.fetch()




            for thisGroup in thisGroupIDList:
                if thisGroup.strGroupID in GroupIDList:
                    GroupIDList.remove(thisGroup.strGroupID)

            for thisGroup in GroupIDList:
                NewGroup = MyGroupIDS()
                NewGroup.writeReference(strinput=Guser.user_id())
                NewGroup.writeGroupID(strinput=thisGroup)
                NewGroup.put()


            if not(vstrGraphApiKey == None):
                try:
                    myGraph = GraphAPI(vstrGraphApiKey)

                    if not(vstrFacebookPost == None):
                        findRequest = GroupPosts.query(GroupPosts.strReference == Guser.user_id())
                        thisGroupPostsLists = findRequest.fetch()

                        if len(thisGroupPostsLists) > 0:
                            thisGroupPost = thisGroupPostsLists[0]
                        else:
                            thisGroupPost = GroupPosts()

                        thisGroupPost.writeReference(strinput=Guser.user_id())
                        thisGroupPost.writeApiKey(strinput=vstrGraphApiKey)
                        thisGroupPost.writeMyPost(strinput=vstrFacebookPost)
                        thisGroupPost.put()

                        self.response.write("Facebook Group Posts successfully created")
                except:
                    self.response.write("theres an Error creating Facebook Group Posts")

class CronFacebookGroupHandler(webapp2.RequestHandler):
    def get(self):

        findRequest = GroupPosts.query()
        thisGroupPostList = findRequest.fetch()

        for thisGroupPost in thisGroupPostList:

            findRequest = MyGroupIDS.query(MyGroupIDS.strReference == thisGroupPost.strReference)
            thisGroupIDList = findRequest.fetch()
            myGraph = GraphAPI(thisGroupPost.strApiKey)
            for thisGroupID in thisGroupIDList:

                try:
                    myGraph.post(path=str(thisGroupID.strGroupID) + '/feed', message=thisGroupPost.strMyPost)
                    thisGroupID.isWorking = True
                except:
                    thisGroupID.isWorking = False

app = webapp2.WSGIApplication([
    ('/social/facebook/groups', FacebookGroupHandler),
    ('/social/facebook/cron/groups', CronFacebookGroupHandler)

], debug=True)