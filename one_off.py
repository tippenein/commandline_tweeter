#!/usr/bin/env python

import os
import tweepy
from config import dotfile_path

try:
  os.remove(dotfile_path)
except:
  pass


CONSUMER_KEY = raw_input("enter your Consumer key: ")
CONSUMER_SECRET = raw_input("enter your Consumer Secret: ")

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth_url = auth.get_authorization_url()
print 'Please authorize: ' + auth_url
verifier = raw_input('PIN: ').strip()
auth.get_access_token(verifier)
print "ACCESS_KEY = '%s'" % auth.access_token.key
print "ACCESS_SECRET = '%s'" % auth.access_token.secret
print "the tweet script will now use %s to fill these keys" % dotfile_path
with open(dotfile_path, 'w') as fd:
  payload = '\n'.join([CONSUMER_KEY, CONSUMER_SECRET, 
                     auth.access_token.key, auth.access_token.secret])
  fd.write(payload)
