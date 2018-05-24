



#!/usr/bin/env python

# Copyright 2007 Google Inc.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import os
import webapp2
import jinja2
from google.appengine.ext import ndb
from google.appengine.api import users


#Jinja Loader
import logging
template_env = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.getcwd()))



class Contact(ndb.Expando):
    strMessageIndex = ndb.IntegerProperty(default=0)
    strFullNames = ndb.StringProperty()
    strEmail = ndb.StringProperty()
    strCell = ndb.StringProperty()
    strSubject = ndb.StringProperty()
    strMessage = ndb.StringProperty()
    strResponded = ndb.BooleanProperty(default=False)

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
