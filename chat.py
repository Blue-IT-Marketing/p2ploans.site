from google.appengine.api import channel
from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.ext.webapp.util import login_required
import cgi
import jinja2
import os
import webapp2
template_env = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.getcwd()))

class ChatUser(ndb.Model):
  """ Stored user model. Should be keyed by the User ID. """
  nickname = ndb.StringProperty()

class HandleConnect(webapp2.RequestHandler):
  """ Send a welcome message and notifies all other users. """
  def post(self):
    user_id = self.request.get('from')
    chat_user = ChatUser.get_by_id(user_id)

    existing_users = ChatUser.query(ChatUser.key != chat_user.key)
    channel.send_message(chat_user.key.string_id(),
                         'Welcome, %s! Other chatters: %d' %
                         (chat_user.nickname, existing_users.count()))
    for existing_user in existing_users:
      channel.send_message(existing_user.key.string_id(),
                           '%s joined' % chat_user.nickname)

class HandleDisconnect(webapp2.RequestHandler):
  """ Deletes the user model and notifies all other users. """
  def post(self):
    user_id = self.request.get('from')
    chat_user = ChatUser.get_by_id(user_id)
    chat_user.key.delete()

    for user in ChatUser.query():
      channel.send_message(user.key.string_id(), '%s left' % chat_user.nickname)

class HandleSend(webapp2.RequestHandler):
  """ When a user sends a message to be echoed to all other users. """
  def post(self):
    user_id = users.get_current_user().user_id()
    chat_user = ChatUser.get_by_id(user_id)

    data = self.request.get('data')
    for recipient in ChatUser.query():
      channel.send_message(recipient.key.string_id(),
                           '%s: %s' % (chat_user.nickname, cgi.escape(data)))

class HandleMain(webapp2.RequestHandler):
  """ Renders index.html an initializes the chat room channel. """

  def get(self):
    Guser = users.get_current_user()
    if Guser:
      chat_user = ChatUser.get_or_insert(Guser.user_id(),nickname = Guser.nickname())

      token = channel.create_channel(chat_user.key.string_id())
      template = template_env.get_template('templates/admin/chat/chat.html')
      self.response.out.write(template.render({ 'token': token }))


class ChatQueueHandler(webapp2.RequestHandler):
  def get(self):
    pass

app = webapp2.WSGIApplication([
  ('/chat', HandleMain),
  ('/send', HandleSend),
  ('/_ah/channel/connected/', HandleConnect),
  ('/_ah/channel/disconnected/', HandleDisconnect),
  ('/_ah/queue/chat-queue', ChatQueueHandler)
], debug=True)
